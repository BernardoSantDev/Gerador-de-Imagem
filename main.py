import streamlit as st          
from dotenv import load_dotenv   
import os                       
import requests                
from io import BytesIO           
from PIL import Image             

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def gerar_imagem_dalle(prompt):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        imagem_url = response.json()['data'][0]['url']
        return imagem_url
    else:
        st.error(f"Erro na geração da imagem. Código: {response.status_code}\nResposta: {response.text}")
        return None




