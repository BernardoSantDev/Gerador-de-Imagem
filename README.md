# 🖼️ Gerador de Imagens com IA (DALL·E 3)

Uma aplicação web interativa construída com **Streamlit** que permite aos usuários gerar imagens de alta qualidade a partir de descrições em texto. 

O projeto consome diretamente a API REST da OpenAI (modelo DALL·E 3), processa a resposta e entrega a imagem renderizada na tela com a opção de download instantâneo em formato `.png`.

---

## ✨ Funcionalidades

* **Geração Text-to-Image:** Interface simples para inserir prompts descritivos.
* **Integração com DALL·E 3:** Utiliza o modelo mais avançado de geração de imagens da OpenAI.
* **Feedback Visual:** Indicador de carregamento dinâmico ("spinner") enquanto a IA processa o pedido.
* **Processamento de Imagem em Memória:** Utiliza `BytesIO` e `PIL` para manipular a imagem sem necessidade de salvar arquivos temporários no servidor.
* **Download Direto:** Botão integrado para baixar a obra gerada com um único clique.

---

## 📸 Capturas de Tela

### 1. Tela Inicial
<img width="1750" height="780" alt="Captura de tela 2026-02-24 003213" src="https://github.com/user-attachments/assets/5fc411c8-7b5b-43ba-b811-6c16be4091f0" />

*Interface limpa e intuitiva aguardando o prompt do usuário.*

### 2. Processamento da IA
<img width="1746" height="788" alt="Captura de tela 2026-02-24 003236" src="https://github.com/user-attachments/assets/fb4b33d7-c022-403d-8a4e-7de1ba241bc7" />

*Feedback visual enquanto a requisição HTTP é feita para os servidores da OpenAI.*

### 3. Resultado e Download
<img width="1732" height="802" alt="Captura de tela 2026-02-24 003302" src="https://github.com/user-attachments/assets/28acc449-e9b2-45d1-a130-c5ae09535fbf" />

*Imagem gerada em alta resolução (1024x1024) pronta para download.*

---

## 🚀 Como instalar e rodar localmente

### 1. Pré-requisitos
* Python 3.8 ou superior.
* Chave de API da OpenAI com créditos disponíveis.

### 2. Clonando o Repositório
```bash
git clone [https://github.com/BernardoSantDev/Gerador-de-Imagem.git](https://github.com/BernardoSantDev/Gerador-de-Imagem.git)
cd Gerador-de-Imagem
```

### 3. Criando o Ambiente Virtual
```bash
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 4. Instalando as Dependências
Crie um arquivo chamado requirements.txt com o seguinte conteúdo:
```bash
streamlit
requests
pillow
python-dotenv
```
Em seguida, instale rodando:
```bash
pip install -r requirements.txt
```

### 5. Configurando a Chave da API
Crie um arquivo .env na raiz do projeto e insira sua chave secreta:
```bash
OPENAI_API_KEY="sk-proj-sua_chave_aqui..."
```

### 6. Executando a Aplicação
```bash
streamlit run app.py
```

O navegador abrirá automaticamente no endereço

---

## 🛠️ Tecnologias Utilizadas

* **Streamlit:** Framework para a interface de usuário web.

* **OpenAI API (GPT-4o):** Motor de Inteligência Artificial generativa.

* **Requests:** Para realizar as chamadas HTTP (POST/GET) à API.

* **Pillow (PIL):** Manipulação e conversão dos dados da imagem.


---

Desenvolvido por Bernardo Silva Sant Ana de Oliveira como projeto do Módulo 2 do curso de Data Science da Codi Academy.
