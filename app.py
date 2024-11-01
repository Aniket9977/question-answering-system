import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
import os
import requests

# Load API token from .env file
load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Check if the API token is available
if not api_token:
    st.error("API token not found. Please set the HUGGINGFACEHUB_API_TOKEN in your .env file.")
else:
    # Setup headers with API token
    headers = {"Authorization": f"Bearer {api_token}"}
    
    # Hugging Face model and API URL
    repo_id = "gpt2"  # Use repo_id instead of model_name for HuggingFaceHub
    api_url = f"https://api-inference.huggingface.co/models/{repo_id}"
    
    # Set up the LangChain components
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="Given the context: {context}, answer the following question: {question}"
    )
    
    llm = HuggingFaceHub(repo_id=repo_id, task="text-generation", huggingfacehub_api_token=api_token)
    qa_chain = LLMChain(llm=llm, prompt=prompt)

    # Streamlit Interface
    st.title("LangChain QA System")
    st.write("Ask questions based on the context provided below.")

    # Input for context
    context = st.text_area("Context", "Enter the context or paragraph here...")

    # Input for question
    question = st.text_input("Question", "Enter your question here...")

    # Button to get the answer
    if st.button("Get Answer"):
        if context and question:
            with st.spinner("Generating answer..."):
                # Get the answer using requests
                response = requests.post(api_url, headers=headers, json={"inputs": f"{context} {question}"})
                
                # Parse and display the response
                if response.status_code == 200:
                    answer = response.json()[0]['generated_text'] if response.json() else "No answer found."
                    st.success("Answer:")
                    st.write(answer)
                else:
                    st.error("Failed to fetch response from Hugging Face API.")
        else:
            st.warning("Please provide both context and a question.")
