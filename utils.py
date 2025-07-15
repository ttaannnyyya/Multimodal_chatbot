# utils.py

# utils.py

import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key="YOUR_KEY")
#I have removed the key for the sake of privacy. You can add yours.

def process_text_input(user_input, model):
    response = model.generate_content(user_input)
    return response.text.strip()

def process_image_input(image: Image.Image, model):
    response = model.generate_content(["Describe this image:", image])
    return response.text.strip()
