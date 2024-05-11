"""
Este script demonstra como usar o Google Gemini para analisar uma imagem.

Primeiro, certifique-se de ter instalado a biblioteca google-generativeai:
  $ pip install google-generativeai
"""

from pathlib import Path  # Para manipular caminhos de arquivo
import google.generativeai as genai  # Biblioteca do Google Gemini

# Configura a API Key do Gemini
genai.configure(api_key="YOUR_API_KEY") # Substitua 'YOUR_API_KEY' pela sua chave

# Configurações do modelo Gemini
generation_config = {
  "temperature": 1,  # Controla a criatividade do modelo (valores mais altos = mais criativo)
  "top_p": 0.95,      # Controla a diversidade das respostas
  "top_k": 0,         # Controla o número de tokens considerados na geração da resposta
  "max_output_tokens": 8192, # Define o tamanho máximo da resposta
}

# Configurações de segurança
safety_settings = [
  {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Inicializa o modelo Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Caminho para a imagem (substitua pelo caminho real da sua imagem)
image_path = Path("/content/7rihkmjk.png")

# Carrega a imagem como bytes
with image_path.open("rb") as image_file:
  image_bytes = image_file.read()

# Cria o histórico da conversa
history = [
  {
    "role": "user",
    "parts": [{"type": "image", "data": image_bytes}] # Envia a imagem
  },
  {
    "role": "user",
    "parts": [{"type": "text", "text": "Analise de imagem, detalhes específicos."}]  # Solicita a análise
  },
]

# Inicia a conversa com o histórico predefinido
convo = model.start_chat(history=history)

# Envia uma nova mensagem
convo.send_message("Há algo mais que você pode me dizer sobre essa imagem?")

# Imprime a resposta do modelo
print(convo.last.text)
