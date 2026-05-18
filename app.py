from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/gerar-perfil-pet', methods=['POST'])
def gerar_perfil_pet():
    dados = request.get_json()

    name        = dados['name']
    gender      = dados['gender']
    breed       = dados['breed']
    description = dados['description']

    prompt = f"""
    Você é um redator carinhoso e criativo de um petshop chamado "Melhor Amigo".
    Crie uma descrição afetiva e personalizada para o perfil de um pet com as seguintes informações:
    
    - Nome: {name}
    - Gênero: {gender}
    - Raça: {breed}
    - {"Sobre ele" if gender == "macho" else "Sobre ela"}: {description}
    
    A descrição deve ter entre 3 e 5 frases, ser escrita em português do Brasil,
    usar um tom acolhedor e alegre, e destacar a personalidade única do animal.
    Retorne apenas o texto da descrição, sem títulos ou formatação extra.
"""
    
    API_KEY = os.environ.get('GEMINI_API_KEY')
    MODEL   = 'gemini-2.5-flash'
    URL     = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'

    resposta = requests.post(URL, json={
        'contents': [
            {
                'parts': [
                    {'text': prompt}
                ]
            }
        ]
    })

    dados_gemini = resposta.json()
    texto = dados_gemini['candidates'][0]['content']['parts'][0]['text']

    return jsonify({'description': texto})

if __name__ == '__main__':
    app.run(debug=True)