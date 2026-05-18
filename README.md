<div align="center">

<h1>🐾 Petshop Melhor Amigo — API</h1>

<p><strong>Back-end da feature de geração de perfil de pet com Inteligência Artificial.</strong></p>

<p>
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini API"/>
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status"/>
</p>

</div>

---

## 📖 Sobre o Projeto

Esta é a API back-end do **Petshop Melhor Amigo**, responsável por intermediar a comunicação entre o front-end e a API do Google Gemini.

O front-end envia os dados do pet (nome, gênero, raça e descrição), a API monta o prompt, chama o Gemini e devolve a descrição gerada — mantendo a chave de API protegida no servidor, longe do navegador do usuário.

> 🔗 Repositório do front-end: [petshop-melhor-amigo](https://pbrunog7.github.io/petshop-melhor-amigo-website/)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask 3.1** — framework web
- **Flask-CORS** — liberação de requisições cross-origin
- **Gunicorn** — servidor de produção (usado no Render)
- **Google Gemini API** — modelo de linguagem para geração de texto
- **python-dotenv** — carregamento de variáveis de ambiente localmente

---

## 🔗 Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/gerar-perfil-pet` | Recebe dados do pet e retorna descrição gerada pela IA |

### Exemplo de requisição

```json
POST /gerar-perfil-pet
Content-Type: application/json

{
  "name": "Thor",
  "gender": "macho",
  "breed": "Golden Retriever",
  "description": "É muito brincalhão, adora dormir no sol"
}
```

### Exemplo de resposta

```json
{
  "description": "Thor é um Golden Retriever cheio de energia e amor para dar..."
}
```

---

## ⚙️ Como Rodar Localmente

> 🌐 API em produção: [petshop-melhor-amigo-api.onrender.com](https://petshop-melhor-amigo-api.onrender.com)

### Pré-requisitos

- Python 3.11+
- pip
- Chave de API do Google Gemini — obtenha gratuitamente em [aistudio.google.com](https://aistudio.google.com)

---

### 1. Clone o repositório

```bash
git clone https://github.com/pbrunog7/petshop-melhor-amigo-api.git
cd petshop-melhor-amigo-api
```

### 2. Crie e ative o ambiente virtual

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

✅ Confirme que está ativado: deve aparecer `(venv)` no início da linha do terminal.

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
GEMINI_API_KEY=sua_chave_aqui
```

> ⚠️ Nunca suba o arquivo `.env` para o GitHub. Ele já está no `.gitignore`.

### 5. Execute o servidor

```bash
python app.py
```

✅ **API rodando em:** `http://localhost:5000`

---

## 🔒 Segurança

- A chave da API do Gemini fica armazenada em variável de ambiente — nunca exposta no código
- CORS configurado para aceitar requisições do front-end hospedado no GitHub Pages
- Em produção, o servidor de desenvolvimento Flask é substituído pelo Gunicorn

---

## 💡 Sobre o Desenvolvimento

Este projeto faz parte do meu portfólio de transição de carreira da Psicologia para o desenvolvimento web. A API foi construída com foco em boas práticas de segurança — separando responsabilidades entre front-end e back-end e protegendo credenciais sensíveis em ambiente de servidor.

---

## 👨‍💻 Autor

**Paulo Gomes** — Desenvolvedor Full Stack  
📍 São Paulo, Brasil  
📧 pbrunog7@gmail.com  
🔗 [github.com/pbrunog7](https://github.com/pbrunog7)

---

## 📄 Licença

Este projeto foi desenvolvido para fins de portfólio.
