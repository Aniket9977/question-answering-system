## LangChain QA System with Streamlit and Hugging Face Integration
This project is a question-answering (QA) system built using LangChain and Hugging Face models, with a Streamlit interface. Users can input a context and ask questions, and the system generates answers based on the provided input.

Features
LangChain Integration: Manages prompt templates and LLM chains to improve response quality.
Hugging Face Model: Uses the GPT-2 model from Hugging Face's model hub for generating answers.
Streamlit UI: Provides a user-friendly web interface for entering context and questions.
Setup Instructions
Prerequisites
Python 3.8 or higher
Hugging Face account and API token (required for accessing Hugging Face-hosted models)


Code Overview
app.py: The main application script where LangChain and Hugging Face integration occurs.
.env: Stores environment variables, including the Hugging Face API token.
requirements.txt: Lists required dependencies for the project.
Example Usage
With the app running, you can input:

Context: "The Eiffel Tower is one of the most famous landmarks in Paris, France. It was built in 1889 for the World's Fair."
Question: "When was the Eiffel Tower built?"
The system will respond with an AI-generated answer based on the context provided.

Troubleshooting
API Token Error: Ensure the .env file is correctly set up, and the token is loaded using python-dotenv.
Model or API Error: Verify that the repo_id (e.g., "gpt2") exists in the Hugging Face model hub and that your API token has the correct permissions.
Context and Question Inputs: Both fields must be filled before clicking "Get Answer"; otherwise, a warning will display.
License
This project is licensed under the MIT License.