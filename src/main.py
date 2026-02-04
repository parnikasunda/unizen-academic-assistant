from vector_store import SimpleVectorStore
from llm_interface import generate_answer

def run_unizen():
    # Initialize store
    store = SimpleVectorStore()

    # Add sample NLP chunks (simulating processed lecture content)
    store.add_chunk(
        1,
        "Tokenization is the process of breaking text into words or subwords in NLP.",
        "nlp_lecture_1.pdf"
    )
    store.add_chunk(
        2,
        "Stemming reduces words to their root form by removing suffixes.",
        "nlp_lecture_2.pdf"
    )
    store.add_chunk(
        3,
        "Lemmatization converts words to their base dictionary form.",
        "nlp_lecture_3.pdf"
    )

    # User query
    question = input("Ask a question about NLP: ")

    # Retrieve relevant content
    result = store.search(question)

    if result:
        answer = generate_answer(result["text"], question)
        print("\nAnswer:")
        print(answer)
        print(f"\n(Source: {result['source']})")
    else:
        print("Sorry, no relevant information found.")

if __name__ == "__main__":
    run_unizen()

