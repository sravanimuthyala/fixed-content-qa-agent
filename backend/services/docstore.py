class DocumentStore:
    def __init__(self):
        self.texts = []

    def add_texts(self, texts: list[str]):
        self.texts.extend(texts)

    def get_all_text(self) -> str:
        return "\n\n".join(self.texts)


doc_store = DocumentStore()
