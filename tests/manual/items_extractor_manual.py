from tests.manual.base_extractor_simplificado import BaseExtractor

import os

PROMPT_PATH = os.path.join(
    "services", "semantic_extraction", "prompts", "items_licitacion", "prompt_items_licitacion_v2.txt"
)

class ItemsLicitacionExtractor(BaseExtractor):
    def concepto(self) -> str:
        return "ITEMS_LICITACION"

    def build_queries(self, doc: dict) -> list[str]:
        return [doc["texto"]]

    def build_prompt(self, doc: dict, query: str) -> str:
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            template = f.read()
        return template.replace("{CONTEXT}", query)

    def parse_output(self, raw_response: str) -> dict:
        import json
        return json.loads(raw_response)
