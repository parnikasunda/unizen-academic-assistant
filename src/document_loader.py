def load_document(file_path):
    """
    Loads a text document and returns its content as a string.
    """
    with open(file_path, "r") as file:
        content = file.read()
    return content


if __name__ == "__main__":
    text = load_document("../data/sample_notes.txt")
    print(text)
#load_document → opens a text file
#reads all the text
#returns it
#the bottom part just prints it (for testing later)
