import streamlit as st
from vector_store import SimpleVectorStore
from llm_interface import generate_answer

st.title("UniZen — Academic Assistant")

# Initialize store
store = SimpleVectorStore()

# Add NLP knowledge chunks
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

# Streamlit input
question = st.text_input("Ask a question about NLP")

if question:
    result = store.search(question)

    if result:
        answer = generate_answer(result["text"], question)
        st.subheader("Answer")
        st.write(answer)
        st.caption(f"Source: {result['source']}")
    else:
        st.write("No relevant information found.")
