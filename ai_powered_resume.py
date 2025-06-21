from flask import Flask, jsonify, request
from flask_cors import CORS
import config
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configure Gemini AI model
genai.configure(api_key=config.API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config  # ✅ Fix typo: was `genaration_config=`
)
#Initialize the App
app=Flask(__name__)
CORS(app)

#Function to interact with Gemini AI

def gemini_generate_response(prompt):
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
    response = chat_session.send_message(prompt)
    return response.text