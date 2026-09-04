import os

class DocumentStore:
    def __init__(self, filepath="uploaded_docs.txt"):
        self.filepath = filepath
        self.texts = []
        self._load_from_disk()

    def _load_from_disk(self):
        """Loads saved texts from disk into memory on startup."""
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    self.texts = content.split("\n\n---DOC_BREAK---\n\n")

    def add_texts(self, texts: list[str]):
        """Adds new texts to memory and appends them to disk."""
        self.texts.extend(texts)
        with open(self.filepath, "a", encoding="utf-8") as f:
            for text in texts:
                f.write(text + "\n\n---DOC_BREAK---\n\n")

    def get_all_text(self) -> str:
        """Returns all aggregated document text."""
        return "\n\n".join(self.texts)

    def clear(self):
        """Clears stored documents in memory and on disk."""
        self.texts = []
        if os.path.exists(self.filepath):
            os.remove(self.filepath)


doc_store = DocumentStore()
