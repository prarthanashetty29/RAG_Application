############################################
# Component #1 - Document Loader
############################################

import streamlit as st
import os

st.set_page_config(layout="wide")

with st.sidebar:
    DOCS_DIR = os.path.abspath("./uploaded_docs")
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
    st.subheader("Add to the Knowledge Base")
    uploaded_files = None  # Initialize to None
    with st.form("my-form", clear_on_submit=True):
        uploaded_files = st.file_uploader("Upload a file to the Knowledge Base:", accept_multiple_files=True)
        submitted = st.form_submit_button("Upload!")

    if uploaded_files and submitted:
        for uploaded_file in uploaded_files:
            with open(os.path.join(DOCS_DIR, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.read())
            st.success(f"File {uploaded_file.name} uploaded successfully!")

############################################
# Component #2 - Embedding Model and LLM
############################################

from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings

llm = ChatNVIDIA(model="mixtral_8x7b")
document_embedder = NVIDIAEmbeddings(model="nvolveqa_40k", model_type="passage")
query_embedder = NVIDIAEmbeddings(model="nvolveqa_40k", model_type="query")

############################################
# Component #3 - Vector Database Store
############################################

from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import FAISS
import pickle

# Initialize vectorstore at the top
vectorstore = None

with st.sidebar:
    use_existing_vector_store = st.radio("Use existing vector store if available", ["Yes", "No"], horizontal=True)

vector_store_path = "vectorstore.pkl"
raw_documents = DirectoryLoader(DOCS_DIR).load()

if not raw_documents:
    st.sidebar.warning("No documents available to process!", icon="⚠️")
else:
    vector_store_exists = os.path.exists(vector_store_path)
    if use_existing_vector_store == "Yes" and vector_store_exists:
        with open(vector_store_path, "rb") as f:
            vectorstore = pickle.load(f)
        st.sidebar.success("Existing vector store loaded successfully.")
    else:
        try:
            with st.sidebar:
                with st.spinner("Splitting documents into chunks..."):
                    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
                    documents = text_splitter.split_documents(raw_documents)

                with st.spinner("Adding document chunks to vector database..."):
                    vectorstore = FAISS.from_documents(documents, document_embedder)

                with st.spinner("Saving vector store"):
                    with open(vector_store_path, "wb") as f:
                        pickle.dump(vectorstore, f)
                st.success("Vector store created and saved.")
        except Exception as e:
            st.sidebar.error(f"Failed to create vector store: {e}")

############################################
# Component #4 - LLM Response Generation and Chat
############################################

st.subheader("Chat with your AI Assistant, Peggy!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful AI assistant named Envie. You will reply to questions only based on the context that you are provided. If something is out of context, you will refrain from replying and politely decline to respond to the user."), ("user", "{input}")]
)
chain = prompt_template | llm | StrOutputParser()

user_input = st.chat_input("Can you tell me what NVIDIA is known for?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if vectorstore is not None:
        retriever = vectorstore.as_retriever()
        docs = retriever.get_relevant_documents(user_input)

        context = ""
        for doc in docs:
            context += doc.page_content + "\n\n"

        augmented_user_input = "Context: " + context + "\n\nQuestion: " + user_input

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            for response in chain.stream({"input": augmented_user_input}):
                full_response += response
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        with st.chat_message("assistant"):
            st.error("Vector store is not initialized. Please check document processing and vector store creation steps.")
