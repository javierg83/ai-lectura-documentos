class BaseExtractor:
    def concepto(self):
        raise NotImplementedError

    def build_queries(self, doc):
        raise NotImplementedError

    def build_prompt(self, doc, query):
        raise NotImplementedError

    def parse_output(self, raw_response):
        raise NotImplementedError

    def run(self, doc):
        query = self.build_queries(doc)[0]
        prompt = self.build_prompt(doc, query)
        from services.llm_service import run_llm_raw
        raw_response = run_llm_raw(prompt)
        parsed = self.parse_output(raw_response)
        return parsed
