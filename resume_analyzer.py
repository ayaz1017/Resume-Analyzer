from flask import Flask, jsonify, request
from flask_cors import CORS
import config
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

#Configure genarative AI Model
