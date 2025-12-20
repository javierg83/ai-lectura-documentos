import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def contar_tokens(texto: str) -> int:
    if not isinstance(texto, str):
        return 0
    return len(enc.encode(texto))

def truncate_chunks_by_tokens(chunks, max_tokens=6000):
    if not isinstance(chunks, list):
        print("[token_utils] ⚠️ chunks no es una lista")
        return []

    total_tokens = 0
    result = []
    for chunk in chunks:
        if not isinstance(chunk, str):
            print(f"[token_utils] ❌ Chunk no es string: {chunk}")
            continue
        chunk_tokens = len(enc.encode(chunk))
        if total_tokens + chunk_tokens > max_tokens:
            break
        result.append(chunk)
        total_tokens += chunk_tokens
    print(f"[token_utils] ✅ Chunks truncados: {len(result)} | Tokens: {total_tokens}")
    return result
