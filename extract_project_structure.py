#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_project_structure.py
Genera un "plan de proyecto" para que una IA entienda la estructura y propósito de cada componente
sin leer archivos completos. Pensado para ejecutarse desde la raíz del proyecto (cwd por defecto).

Salidas:
- Markdown: PROJECT_PLAN.md (árbol + resúmenes)
- JSON:     project_plan.json (estructura detallada para IA)

Uso:
    # desde la raíz del repo
    python extract_project_structure.py
    # o con opciones
    python extract_project_structure.py \
        --root . \
        --max-bytes 6000 \
        --out-md PROJECT_PLAN.md \
        --out-json project_plan.json \
        --follow-gitignore \
        --extra-ignore ".env,.DS_Store,dist,build"
"""

import os
import re
import sys
import ast
import json
import argparse
import hashlib
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

# ---------- Config por defecto ----------
DEFAULT_IGNORE_DIRS = {
    ".git", ".hg", ".svn", ".venv", "venv", "Lib", "Scripts", "archivos", "archivos_entrada_temp", "archivos_texto", "__pycache__", "node_modules",
    ".mypy_cache", ".pytest_cache", ".ruff_cache", ".idea", ".vscode", ".tox",
    "dist", "build", ".eggs", "*.egg-info", "1"
}
DEFAULT_MAX_BYTES = 6000  # máximo a leer por archivo para heurísticas
TEXT_EXTS = {
    ".py", ".md", ".rst", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini",
    ".cfg", ".env", ".gitignore", ".dockerignore", ".html", ".htm", ".css",
    ".js", ".ts", ".tsx", ".jsx", ".sql", ".sh", ".bat", ".ps1", ".xml",
    ".jinja", ".j2"
}

LANG_BY_EXT = {
    ".py": "Python",
    ".md": "Markdown",
    ".rst": "reStructuredText",
    ".txt": "Text",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",
    ".ini": "INI",
    ".cfg": "Config",
    ".env": "Env",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript/React",
    ".jsx": "JavaScript/React",
    ".sql": "SQL",
    ".sh": "Shell",
    ".bat": "Batch",
    ".ps1": "PowerShell",
    ".xml": "XML",
    ".jinja": "Jinja",
    ".j2": "Jinja",
    ".dockerfile": "Dockerfile",
    "dockerfile": "Dockerfile"
}

FRAMEWORK_HINTS = [
    ("fastapi", "FastAPI (API web)"),
    ("flask", "Flask (API web)"),
    ("django", "Django (framework web)"),
    ("sqlalchemy", "SQLAlchemy (ORM)"),
    ("alembic", "Alembic (migraciones)"),
    ("pydantic", "Pydantic (modelos/validación)"),
    ("jinja2", "Jinja2 (templates)"),
    ("uvicorn", "Uvicorn (ASGI server)"),
    ("gunicorn", "Gunicorn (WSGI/ASGI server)"),
    ("celery", "Celery (jobs/worker)"),
    ("redis", "Redis (cache/colas)"),
    ("httpx", "HTTPX (cliente HTTP)"),
    ("requests", "Requests (cliente HTTP)"),
    ("pytest", "Pytest (tests)"),
    ("unittest", "Unittest (tests)"),
    ("htmx", "HTMX (interacción HTML)"),
]

ROLE_GUESSES = [
    (re.compile(r"(main\.py|app\.py|wsgi\.py|asgi\.py)$"), "Punto de entrada de la app/servidor"),
    (re.compile(r"(settings|config|configuration)\.py$"), "Configuración"),
    (re.compile(r"(router|routes|endpoints)\.py$"), "Rutas/Endpoints"),
    (re.compile(r"(model|models|schemas|dto)\.py$"), "Modelos/Esquemas"),
    (re.compile(r"(service|services|usecase|use_case)\.py$"), "Servicios/Lógica de negocio"),
    (re.compile(r"(repo|repository|repositories|dao)\.py$"), "Capa de acceso a datos / Repositorios"),
    (re.compile(r"(utils?|helpers?)\.py$"), "Utilidades"),
    (re.compile(r"(auth|security)\.py$"), "Autenticación/Seguridad"),
    (re.compile(r"(tasks?|worker|celery)\.py$"), "Tareas/Workers"),
    (re.compile(r"(tests?|test_.*\.py)$"), "Pruebas"),
    (re.compile(r"(alembic|migrations?)"), "Migraciones"),
    (re.compile(r"(templates?/.*\.(html|jinja|j2))"), "Templates HTML"),
    (re.compile(r"(static/|assets/)"), "Archivos estáticos (CSS/JS/Imágenes)"),
    (re.compile(r"(dockerfile|compose\.yml|compose\.yaml)", re.I), "Infra/Docker"),
    (re.compile(r"(requirements\.txt|poetry\.lock|pyproject\.toml)"), "Dependencias"),
    (re.compile(r"readme\.(md|rst|txt)$", re.I), "Documentación"),
]

# ---------- Utilidades ----------
def norm_ext(path: str) -> str:
    base = os.path.basename(path)
    if base.lower() == "dockerfile":
        return "dockerfile"
    return os.path.splitext(base)[1].lower()

def is_probably_text(path: str) -> bool:
    ext = norm_ext(path)
    return ext in TEXT_EXTS or ext in LANG_BY_EXT

def sha1_of_string(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8", errors="ignore")).hexdigest()

def safe_read_head(path: str, max_bytes: int) -> str:
    try:
        with open(path, "rb") as f:
            blob = f.read(max_bytes)
        for enc in ("utf-8", "latin-1", "cp1252"):
            try:
                return blob.decode(enc, errors="ignore")
            except Exception:
                continue
        return blob.decode("utf-8", errors="ignore")
    except Exception:
        return ""

def count_loc(path: str) -> int:
    if not is_probably_text(path):
        return 0
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def extract_python_docstring_and_symbols(src: str) -> Tuple[Optional[str], List[str], List[str]]:
    """Devuelve (docstring_modulo, clases, funciones)"""
    try:
        tree = ast.parse(src)
        doc = ast.get_docstring(tree)
        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        funcs = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        return doc, classes, funcs
    except Exception:
        return None, [], []

def first_comment_lines(text: str, max_lines: int = 8) -> str:
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines[:40]):
        l = line.strip()
        if not l:
            continue
        if l.startswith(("#", "//", "/*", "*", "<!--")) or i == 0:
            out.append(line)
        if len(out) >= max_lines:
            break
    return "\n".join(out)

def detect_frameworks(text: str) -> List[str]:
    text_low = text.lower()
    hits = []
    for key, label in FRAMEWORK_HINTS:
        if key in text_low:
            hits.append(label)
    return hits

def guess_role(relpath: str, text: str) -> List[str]:
    hints = []
    for regex, label in ROLE_GUESSES:
        if regex.search(relpath.replace("\\", "/")):
            hints.append(label)
    if "from fastapi" in text or "import fastapi" in text:
        hints.append("Endpoint/Lógica FastAPI")
    if "sqlalchemy" in text:
        hints.append("Modelo/ORM SQLAlchemy")
    if "pydantic" in text:
        hints.append("Modelo/Validación Pydantic")
    if "jinja2" in text:
        hints.append("Render de templates Jinja2")
    return sorted(set(hints))

def load_gitignore(root: str) -> List[str]:
    path = os.path.join(root, ".gitignore")
    patterns = []
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    patterns.append(line)
        except Exception:
            pass
    return patterns

def match_ignore(name: str, ignore_set: set, extra_patterns: List[str]) -> bool:
    if name in ignore_set:
        return True
    for pat in extra_patterns:
        pat = pat.strip()
        if not pat:
            continue
        if "*" in pat:
            regex = "^" + pat.replace(".", r"\.").replace("*", ".*") + "$"
            if re.match(regex, name):
                return True
        else:
            if name == pat or name.endswith("/" + pat) or name.startswith(pat + "/"):
                return True
    return False

# ---------- Núcleo ----------
def walk_project(root: str,
                 follow_gitignore: bool,
                 extra_ignore: List[str],
                 max_bytes: int) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    git_patterns = load_gitignore(root) if follow_gitignore else []
    ignore_base = set(DEFAULT_IGNORE_DIRS)

    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == ".":
            rel_dir = ""

        # filtrar carpetas
        pruned = []
        for d in list(dirnames):
            if match_ignore(d, ignore_base, git_patterns + extra_ignore):
                pruned.append(d)
        for d in pruned:
            dirnames.remove(d)

        # agregar directorio
        items.append({
            "type": "dir",
            "relpath": rel_dir.replace("\\", "/"),
            "name": os.path.basename(dirpath) if rel_dir else os.path.basename(root.rstrip(os.sep)),
        })

        # archivos
        for fname in filenames:
            relpath = os.path.join(rel_dir, fname).replace("\\", "/") if rel_dir else fname
            if match_ignore(fname, set(), git_patterns + extra_ignore):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                size = os.path.getsize(fpath)
            except Exception:
                size = None
            ext = norm_ext(fpath)
            lang = LANG_BY_EXT.get(ext, None)
            text = safe_read_head(fpath, max_bytes=max_bytes)
            loc = count_loc(fpath) if is_probably_text(fpath) else 0
            role = guess_role(relpath, text)
            frameworks = detect_frameworks(text)
            doc = None
            classes, funcs = [], []
            if ext == ".py" and is_probably_text(fpath):
                doc, classes, funcs = extract_python_docstring_and_symbols(text)

            comment_hint = None
            if ext != ".py" and is_probably_text(fpath):
                comment_hint = first_comment_lines(text)

            items.append({
                "type": "file",
                "relpath": relpath,
                "name": fname,
                "size_bytes": size,
                "loc": loc,
                "ext": ext,
                "language": lang,
                "role_hints": role,
                "framework_hints": frameworks,
                "python_docstring": doc,
                "python_classes": classes,
                "python_functions": funcs,
                "head_comment_hint": comment_hint,
                "sha1_head": sha1_of_string(text) if text else None,
            })
    return items

def aggregate_stats(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    lang_counts: Dict[str, int] = {}
    total_files = 0
    total_loc = 0
    for it in items:
        if it["type"] != "file":
            continue
        total_files += 1
        total_loc += it.get("loc", 0) or 0
        lang = it.get("language") or "Other"
        lang_counts[lang] = lang_counts.get(lang, 0) + 1
    return {
        "total_files": total_files,
        "total_loc": total_loc,
        "by_language": dict(sorted(lang_counts.items(), key=lambda kv: (-kv[1], kv[0])))
    }

def read_dependency_overview(root: str) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    req = os.path.join(root, "requirements.txt")
    if os.path.exists(req):
        try:
            with open(req, "r", encoding="utf-8", errors="ignore") as f:
                deps = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]
            data["requirements.txt"] = deps[:200]
        except Exception:
            pass
    pyp = os.path.join(root, "pyproject.toml")
    if os.path.exists(pyp):
        try:
            with open(pyp, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            tool_poetry = re.findall(r"\[tool\.poetry\.dependencies\](.*?)\n\[", content + "\n[END]", re.S)
            tool_pdm = re.findall(r"\[project\](.*?)\n\[", content + "\n[END]", re.S)
            snippet = content[:4000]
            data["pyproject.toml_snippet"] = snippet
            if tool_poetry:
                data["pyproject_poetry_dependencies_block"] = tool_poetry[0][:2000]
            if tool_pdm:
                data["pyproject_project_block"] = tool_pdm[0][:2000]
        except Exception:
            pass
    dockerfile = os.path.join(root, "Dockerfile")
    if os.path.exists(dockerfile):
        try:
            with open(dockerfile, "r", encoding="utf-8", errors="ignore") as f:
                data["Dockerfile_snippet"] = f.read()[:3000]
        except Exception:
            pass
    for name in ("compose.yml", "compose.yaml", "docker-compose.yml", "docker-compose.yaml"):
        path = os.path.join(root, name)
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    data[f"{name}_snippet"] = f.read()[:3000]
            except Exception:
                pass
    return data

def make_tree_markdown(items: List[Dict[str, Any]]) -> str:
    from collections import defaultdict

    tree = {}

    def insert_path(path: str, entry: Dict[str, Any]):
        parts = path.strip("/").split("/")
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part + "/", {})
        # Si está en raíz, usar clave especial "__root__"
        key = "__root__" if len(parts) == 1 else "__files__"
        node.setdefault(key, []).append(entry)

    # Insertar archivos
    for item in items:
        if item["type"] == "file":
            insert_path(item["relpath"], item)

    # Insertar carpetas explícitamente
    for item in items:
        if item["type"] == "dir":
            parts = item["relpath"].strip("/").split("/")
            node = tree
            for part in parts:
                node = node.setdefault(part + "/", {})

    # Render recursivo
    def render(node, indent=""):
        lines = []
        if "__root__" in node:
            for f in sorted(node["__root__"], key=lambda x: x["name"].lower()):
                lines.append(f"{indent}  └─ 📄 {f['name']}")
        for key in sorted(k for k in node if k not in {"__files__", "__root__"}):
            lines.append(f"{indent}📁 {key}")
            lines.extend(render(node[key], indent + "  "))
        if "__files__" in node:
            for f in sorted(node["__files__"], key=lambda x: x["name"].lower()):
                lines.append(f"{indent}  └─ 📄 {f['name']}")
        return lines

    return "\n".join(render(tree))


def summarize_item_brief(it: Dict[str, Any]) -> str:
    parts = []
    if it.get("language"):
        parts.append(it["language"])
    if it.get("role_hints"):
        parts.append("; ".join(it["role_hints"]))
    if it.get("framework_hints"):
        parts.append("Tech: " + ", ".join(sorted(set(it["framework_hints"]))))
    return " — ".join(parts) if parts else "Archivo"

def make_markdown_report(root: str,
                         items: List[Dict[str, Any]],
                         stats: Dict[str, Any],
                         deps: Dict[str, Any]) -> str:
    tree_md = make_tree_markdown(items)
    created = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    out: List[str] = []
    out.append(f"# Project Plan — Resumen de Componentes\n")
    out.append(f"_Generado automáticamente el {created}_\n")
    out.append(f"- **Raíz analizada:** `{root}`")
    out.append(f"- **Archivos (texto y binarios):** {stats['total_files']}")
    out.append(f"- **LOC (estimado):** {stats['total_loc']}\n")

    out.append("## Lenguajes / Tipos (conteo)")
    if stats["by_language"]:
        for lang, cnt in stats["by_language"].items():
            out.append(f"- {lang}: {cnt}")
    else:
        out.append("- (sin detecciones)")
    out.append("")

    out.append("## Árbol del proyecto (resumido)")
    out.append("```\n" + tree_md + "\n```\n")

    out.append("## Dependencias & Infra (resumen)")
    if "requirements.txt" in deps:
        out.append("**requirements.txt (top)**")
        sample = deps["requirements.txt"][:20]
        out.append("```\n" + "\n".join(sample) + ("\n..." if len(deps["requirements.txt"]) > 20 else "") + "\n```")
    if "pyproject.toml_snippet" in deps:
        out.append("**pyproject.toml (snippet)**")
        out.append("```toml\n" + deps["pyproject.toml_snippet"] + "\n```")
    for k, v in deps.items():
        if k.endswith("_snippet") and k not in ("pyproject.toml_snippet",):
            out.append(f"**{k}**")
            fence = "```yaml" if k.endswith((".yml_snippet", ".yaml_snippet")) else "```"
            out.append(f"{fence}\n{v}\n```")
    out.append("")

    out.append("## Componentes y propósito (por archivo)")
    for it in items:
        if it["type"] != "file":
            continue
        rel = it["relpath"]
        brief = summarize_item_brief(it)
        size = it.get("size_bytes")
        loc = it.get("loc")
        out.append(f"### `{rel}`")
        metas = []
        if brief:
            metas.append(brief)
        if size is not None:
            metas.append(f"tamaño: {size} bytes")
        if loc:
            metas.append(f"LOC aprox: {loc}")
        if metas:
            out.append("- " + " | ".join(metas))
        if it.get("python_docstring"):
            out.append("**Docstring módulo (resumen):**")
            doc = it["python_docstring"].strip()
            if len(doc) > 400:
                doc = doc[:400] + "..."
            out.append("> " + doc.replace("\n", "\n> "))
        if it.get("python_classes") or it.get("python_functions"):
            if it.get("python_classes"):
                classes = ", ".join(it["python_classes"][:20])
                out.append(f"- Clases: {classes}" + (" ..." if len(it["python_classes"]) > 20 else ""))
            if it.get("python_functions"):
                funcs = ", ".join(it["python_functions"][:25])
                out.append(f"- Funciones: {funcs}" + (" ..." if len(it["python_functions"]) > 25 else ""))
        if it.get("head_comment_hint"):
            out.append("**Encabezado/comentario (snippet):**")
            snippet = it["head_comment_hint"]
            if len(snippet) > 400:
                snippet = snippet[:400] + "..."
            out.append("```\n" + snippet + "\n```")
        out.append("")
    return "\n".join(out)

def make_json_report(root: str,
                     items: List[Dict[str, Any]],
                     stats: Dict[str, Any],
                     deps: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "generated_utc": datetime.utcnow().isoformat() + "Z",
        "root": os.path.abspath(root),
        "stats": stats,
        "dependencies_overview": deps,
        "items": items
    }

# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="Genera un plan/resumen del proyecto para IA.")
    parser.add_argument("--root", default=".", help="Ruta a la carpeta del proyecto (por defecto, cwd)")
    parser.add_argument("--out-md", default="PROJECT_PLAN.md", help="Archivo de salida Markdown")
    parser.add_argument("--out-json", default="project_plan.json", help="Archivo de salida JSON")
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES, help="Máximo de bytes a leer por archivo para heurísticas")
    parser.add_argument("--follow-gitignore", action="store_true", help="Respetar patrones de .gitignore")
    parser.add_argument("--extra-ignore", default="", help="Lista separada por comas de rutas o patrones a ignorar (e.g., '.env,dist,build')")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"✗ La ruta no es un directorio: {root}", file=sys.stderr)
        sys.exit(1)

    max_bytes = max(512, int(args.max_bytes))
    extra_ignore = [p.strip() for p in args.extra_ignore.split(",") if p.strip()]

    print(f"• Escaneando: {root}")
    items = walk_project(root, follow_gitignore=args.follow_gitignore, extra_ignore=extra_ignore, max_bytes=max_bytes)
    stats = aggregate_stats(items)
    deps = read_dependency_overview(root)

    md = make_markdown_report(root, items, stats, deps)
    js = make_json_report(root, items, stats, deps)

    md_path = os.path.join(root, args.out_md)
    js_path = os.path.join(root, args.out_json)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    with open(js_path, "w", encoding="utf-8") as f:
        json.dump(js, f, ensure_ascii=False, indent=2)

    print("✓ Listo. Escribí:")
    print(f"  - {md_path}")
    print(f"  - {js_path}")

if __name__ == "__main__":
    main()
