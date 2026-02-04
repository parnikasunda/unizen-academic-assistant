# This module will interact with the language model to generate responses
def generate_answer(context, question):
    """
    Generates an answer based on retrieved context.
    This simulates how a language model would respond.
    """
    if not context:
        return "Sorry, I could not find relevant information in the provided documents."

    answer = (
        "Based on the academic documents, here is the relevant information:\n\n"
        f"{context}"
    )
    return answer


if __name__ == "__main__":
    sample_context = "Tokenization is the process of breaking text into words or subwords in NLP."
    sample_question = "What is tokenization?"

    response = generate_answer(sample_context, sample_question)
    print(response)

