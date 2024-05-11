<a href="https://git.io/typing-svg" target=_blank rel="nofollow noopener noreferrer"><img src="https://readme-typing-svg.demolab.com?font=Poppins&size=44&height=100&duration=1600&pause=1000&color=009680&width=750&lines=Desafio de Código Alura +👨‍💻; Utilizar API do Google IA Studio 🤖 ; " alt="Typing SVG" data-canonical-src="https://readme-typing-svg.demolab.com?font=Poppins&size=44&duration=1600&pause=1000&color=008000&width=435&lines=Fala+Devs!+Sejam+bem-vindos!;Web+Developers...;Mobile+Developers...;FullStack..https://emresitesweb.com.br/wp-content/uploads/2023/11/gitironman01.png.;Systems+Analysts...;...and students!" style="max-width: 100%;">
# Como utilizar uma chave API do Google IA Studio para Analisar Imagens fazendo a requisição dentro do código em python👩‍💻
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ricardoalexandreprofissional/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ralexandrecode)
[![AWS](https://img.shields.io/badge/AWS-000.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://www.credly.com/users/ricardoalexandre.profissional/badges)
[![My profile DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DER?style=for-the-badge)](https://www.dio.me/users/ricardoalexandre_profissional)

## 📒 Descrição
Este guia detalha os passos necessários para configurar a API do Gemini e utilizar a inteligência artificial por meio de um código Python executado no ambiente do Google Colab. O propósito é avaliar a funcionalidade da API, que permite a comunicação entre prompts e imagens selecionadas com a inteligência do Gemini para descrever ou analisar objetos diretamente através de código, em vez de depender de um navegador convencional. Esta abordagem é especialmente vantajosa, pois possibilita a personalização de um chat de IA exclusivo para nossas necessidades.

## 🧐 Processo de Criação do código.

A seguir os passos que devem ser seguidos na criação do código python:

1. Importar as bibliotecas: Path para trabalhar com caminhos de arquivo e google.generativeai para o Gemini.
Configura a API Key: Substitua YOUR_API_KEY pela sua chave de API do Gemini.

2. Definir as configurações do modelo: Controla a criatividade, diversidade, tamanho máximo da resposta, etc.
Define as configurações de segurança: Bloqueia conteúdo inadequado.

3. Inicializar o modelo: Cria uma instância do modelo Gemini.
Carrega a imagem: Lê a imagem do disco como bytes.

4. Criar o histórico da conversa: Define as mensagens iniciais da conversa, incluindo o envio da imagem e a solicitação de análise.
Inicia a conversa: Cria um objeto de conversa com o histórico predefinido.

5. Enviar uma mensagem: Envia uma nova mensagem para o modelo.
Imprime a resposta: Mostra a resposta do modelo.

## 🐍 Esse é um exemplo de código que pode ser inicialmente gerado pelo Google IA Studio e depois alterado.
````markdown
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

````
## 📸 Imagem do código em execução

![Texto alternativo](https://github.com/ralexandrecode/api-gemini/blob/main/api1.png)

## 💭 Conclusão

Esse é o ponto de partida para criar novos programas com funcionalidades incorporadas com as IAs. Aprimore o código e tenha um programa em python poderoso que utiliza a inteligência artificial para interegir e resolver problemas.

# Conecte-se comigo: 🤝🏽
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ricardoalexandreprofissional/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ralexandrecode)
[![AWS](https://img.shields.io/badge/AWS-000.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://www.credly.com/users/ricardoalexandre.profissional/badges)
[![My profile DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DER?style=for-the-badge)](https://www.dio.me/users/ricardoalexandre_profissional)
