# Streamlit RAG Chatbot

This is a Streamlit-based chatbot application that uses Retrieval-Augmented Generation (RAG) to answer user questions. It leverages OpenAI's API and a vector database (ChromaDB) to provide contextually relevant answers.

## Features
- Conversational chatbot interface
- Retrieval of relevant documents from a vector database
- Adjustable creativity (temperature) and context size via sidebar sliders

## Setup Instructions

1. **Install dependencies**
   - Make sure you have Python 3.8+
   - Install required packages:
     ```bash
     pip install streamlit openai chromadb rich
     ```
   - (You may need to install other dependencies used in your project, such as `topic_categorization`, `vector_store`, etc.)

2. **Set your OpenAI API key**
   - Export your API key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your-key-here
     ```
   - Or set it in your environment as appropriate for your OS.

3. **Prepare the vector database**
   - Ensure your ChromaDB vector database is initialized and contains relevant documents for retrieval.

4. **Run the app**
   - From the project directory, run:
     ```bash
     streamlit run chatbot.py
     ```

## Usage Instructions

- Type your message in the chat input box at the bottom of the page.
- The chatbot will retrieve relevant context from the vector database and generate a response using OpenAI's API.

### Sidebar Settings
- **Temperature (creativity):**
  - Controls the randomness/creativity of the chatbot's responses.
  - Range: 0.0 (deterministic) to 1.0 (very creative). Default is 0.7.
- **Number of relevant texts:**
  - Sets how many relevant documents are retrieved from the vector database to provide context for each answer.
  - Range: 0 to 10. Default is 5.

Adjust these sliders to experiment with the chatbot's behavior and the amount of context it uses.

## Notes
- The chatbot is designed to handle multiple user messages and provide answers as if it "knows" the context, not just repeating retrieved text.
- You can extend or modify the retrieval and embedding logic as needed for your use case.

---

For any issues or questions, please refer to the code or contact the project maintainer. 