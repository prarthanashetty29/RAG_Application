# INFO6105_FinalProject_RAG

## Retriever-Augmented Generation (RAG) Application
 # Introduction
Welcome to the Retriever-Augmented Generation (RAG) Application, an advanced AI-powered platform designed to simplify the process of information retrieval from extensive document sets. Utilizing state-of-the-art language processing models, RAG enables users to extract data and answer queries through a seamless conversational interface.

# Features
Conversational AI Assistant: Ask questions and get precise information extracted from your uploaded documents.
Vector Database Store: Efficiently encoded and indexed documents for rapid information retrieval.
Document Upload Facility: Easily upload and manage documents within the application.
Streamlit Web Interface: A user-friendly and interactive interface built with Streamlit for a smooth experience.

# Quick Start
 # Setting up the Environment:
 Python needs to be installed and then set up a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
 # Install Dependencies:
  Installed all necessary dependencies by running requirements file with all necessary dependencies:
  pip install -r requirements.txt
 # Run the Application:
  Start the Streamlit application with the following command:
  streamlit run app.py
 # Access the App:
 Navigated to http://localhost:8501 in the web browser to access the app.
 # Project Structure
-app.py: The main application file containing Streamlit UI components.
-requirements.txt: A list of Python libraries required for the project.
-vectorstore.pkl: Serialized file where document vectors are stored.
-./uploaded_docs: Default directory where uploaded documents are stored.
 # Documentation
For detailed information about the application's architecture, usage, and contributing guidelines, please refer to the Documentation uploaded on Canvas

License
This project is licensed under the MIT License 
MIT License

Copyright (c) 2024 prarthanashetty29

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
