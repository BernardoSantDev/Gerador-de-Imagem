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

st.set_page_config(page_title="Gerador de Imagens com IA", layout="centered")

st.title("🖼️ Gerador de Imagens com DALL·E")
st.write("Descreva a imagem que você deseja gerar abaixo e clique em **Gerar Imagem**:")

# 🔸 Input de texto
prompt = st.text_input("📝 Descreva sua imagem:")

# 🔸 Botão
gerar = st.button("🚀 Gerar Imagem")

# 🔸 Quando clicar no botão
if gerar:
    if not prompt:
        st.warning("⚠️ Por favor, escreva uma descrição!")
    else:
        with st.spinner("🧠 A IA está gerando sua imagem..."):
            imagem_url = gerar_imagem_dalle(prompt)

        if imagem_url:
            response = requests.get(imagem_url)
            imagem = Image.open(BytesIO(response.content))

            st.image(imagem, caption="🖼️ Sua imagem gerada pela IA", use_container_width=True)

            buffer = BytesIO()
            imagem.save(buffer, format="PNG")
            buffer.seek(0)

            st.download_button(
                label="⬇️ Baixar Imagem",
                data=buffer,
                file_name="imagem_gerada.png",
                mime="image/png"
            )




