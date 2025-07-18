# Tech Challenge - API de Livros

Este projeto é parte do Tech Challenge da FIAP para a fase Machine Learning Engineering.

O objetivo é criar uma API pública que sirva dados de livros extraídos do site [Books to Scrape](https://books.toscrape.com/), com potencial de uso para cientistas de dados e modelos de machine learning.

---

## 📦 Como rodar o projeto localmente

1. Clone o repositório:
git clone https://github.com/johnrobert-oli/tech-challenge-books.git

cpp
Copiar
Editar

2. Crie um ambiente virtual e ative:
python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

csharp
Copiar
Editar

3. Instale as dependências:
pip install -r requirements.txt

markdown
Copiar
Editar

4. Rode o script de scraping:
python scripts/scraping.py

css
Copiar
Editar

5. Rode a API Flask:
python api/app.py

yaml
Copiar
Editar

---

## 🚀 Endpoints disponíveis

- **GET /** → Verificar status da API  
- **GET /api/v1/books** → Lista todos os livros  
- **GET /api/v1/books/<id>** → Detalhe de um livro pelo índice  
- **GET /api/v1/categories** → Lista todas as categorias  
- **GET /api/v1/books/search?title=...&category=...** → Busca por título ou categoria

---

## 💡 Exemplo de uso

- `http://127.0.0.1:5000/api/v1/books/0` → Primeiro livro  
- `http://127.0.0.1:5000/api/v1/categories` → Categorias  
- `http://127.0.0.1:5000/api/v1/books/search?title=sapiens` → Busca "sapiens"

---

## 📊 Diagrama arquitetural

(Sugestão: insira aqui uma imagem do diagrama ou descreva o fluxo)
Scraping → CSV → API Flask → Usuário final

yaml
Copiar
Editar

---

## 🌍 Deploy (quando disponível)

(Adicione aqui o link do Render ou Heroku quando fizer o deploy)

---

## 👨‍💻 Autor

johnrobert-oli