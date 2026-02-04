# This module will manage vector storage and similarity search
class SimpleVectorStore:
    """
    A simple in-memory store for text chunks.
    Each chunk is stored with an ID and source document.
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
#just to show structure
if __name__ == "__main__":
    vector_store = SimpleVectorStore()

    vector_store.add_chunk(
        chunk_id=1,
        text="Tokenization is the process of breaking text into smaller units.",
        source="nlp_lecture_1.pdf"
    )

    vector_store.add_chunk(
        chunk_id=2,
        text="Stemming reduces words to their root form.",
        source="nlp_lecture_2.pdf"
    )

    for cid, data in vector_store.get_all_chunks().items():
        print(f"Chunk {cid} from {data['source']}: {data['text']}")
