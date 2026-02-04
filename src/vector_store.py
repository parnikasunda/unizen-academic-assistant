class SimpleVectorStore:
    """
    A simple in-memory store for text chunks.
    Each chunk is stored with an ID, text, and source document.
    """

    def __init__(self):
        self.store = {}

    def add_chunk(self, chunk_id, text, source):
        self.store[chunk_id] = {
            "text": text,
            "source": source
        }

    def get_all_chunks(self):
        return self.store

    def search(self, query):
        """
        Finds the most relevant chunk based on word overlap.
        """
        query_words = set(query.lower().split())
        best_match = None
        max_overlap = 0

        for chunk in self.store.values():
            chunk_words = set(chunk["text"].lower().split())
            overlap = len(query_words.intersection(chunk_words))
            

            if overlap > max_overlap:
                max_overlap = overlap
                best_match = chunk

        return best_match

if __name__ == "__main__":
    store = SimpleVectorStore()

    store.add_chunk(
        1,
        "Tokenization is the process of breaking text into smaller units.",
        "nlp_lecture_1.pdf"
    )
    store.add_chunk(
        2,
        "Stemming reduces words to their root form.",
        "nlp_lecture_2.pdf"
    )

    query = "What is tokenization?"
    result = store.search(query)

    if result:
        print(f"Answer from {result['source']}: {result['text']}")
    else:
        print("No relevant information found.")

