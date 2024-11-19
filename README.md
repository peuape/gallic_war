
# Gallic War Query Assistant

The **Gallic War Query Assistant** is a Streamlit-based application that allows users to ask questions about **Book 7 of *Commentaries on the Gallic War*** by Julius Caesar. It uses OpenAI's GPT-based model to retrieve and answer questions based on a text file (`chapter7.txt`) containing the content of Book 7.

---

## Features

- **Document Embedding**: Embeds the document using OpenAI embeddings.
- **Vector Store**: Efficient storage and retrieval of document embeddings using FAISS.
- **Question Answering**: Answers questions by retrieving relevant context from the document.
- **Streamlit UI**: User-friendly interface for querying the assistant.

---

## Installation

1. Clone the repository or download the code.
2. Ensure you have Python 3.8+ installed.
3. Install the required libraries:
   ```bash
   pip install streamlit langchain langchain-community langchain-openai faiss-cpu
   ```

---

## How to Run

1. Make sure the text content of Book 7 is saved as `chapter7.txt` in the same directory as the script.
2. Launch the Streamlit app:
   ```bash
   streamlit run main.py
   ```

---

## How to Use

1. **Set Your OpenAI API Key**:  
   - Visit [OpenAI API](https://platform.openai.com/api-keys) to get your API key.  
   - Enter it in the input box in the app.
   
2. **Enter Your Query**:  
   - Type your question in the second input box and click **Submit**.

3. **Receive Answers**:  
   - The assistant retrieves and displays answers based on the text file.

---

## Limitations

- **Scope**: Only supports **Book 7** of the *Commentaries on the Gallic War* as this is the only text included in the current version.
- **Accuracy**: The system relies on the provided content and cannot guarantee accurate responses outside this context.
- **API Usage**: Requires an OpenAI API key to function, and usage may incur costs based on API consumption.

---

## Example Questions

- "Who is Vercingetorix's father?"
- "Which city did Carnutes assault first?"

---



