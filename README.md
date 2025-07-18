# 📚 Tech Challenge - API de Livros

Este projeto faz parte do **Tech Challenge da FIAP** para a fase Machine Learning Engineering.

🎯 **Objetivo:** Criar uma API pública que serve dados de livros extraídos do site [Books to Scrape](https://books.toscrape.com/), com potencial de uso para cientistas de dados e modelos de machine learning.

---

## 🚀 Como rodar o projeto localmente

1️⃣ **Clone o repositório**
git clone https://github.com/johnrobert-oli/tech-challenge-books.git

cpp
Copiar
Editar

2️⃣ **Crie o ambiente virtual e ative**
python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

csharp
Copiar
Editar

3️⃣ **Instale as dependências**
pip install -r requirements.txt

markdown
Copiar
Editar

4️⃣ **Rode o script de scraping**
python scripts/scraping.py

css
Copiar
Editar

5️⃣ **Rode a API Flask**
python api/app.py

yaml
Copiar
Editar

---

## 📡 Endpoints disponíveis

✅ **GET /** → Verificar status da API  
✅ **GET /api/v1/books** → Listar todos os livros  
✅ **GET /api/v1/books/<id>** → Consultar um livro pelo índice  
✅ **GET /api/v1/categories** → Listar todas as categorias  
✅ **GET /api/v1/books/search?title=...&category=...** → Buscar por título e/ou categoria

---

## 💡 Exemplos de uso

- `http://127.0.0.1:5000/api/v1/books/0` → Primeiro livro  
- `http://127.0.0.1:5000/api/v1/categories` → Categorias  
- `http://127.0.0.1:5000/api/v1/books/search?title=sapiens` → Buscar livros com "sapiens" no título

---

## 🛠️ Diagrama arquitetural

[ Scraping.py ] → [ books.csv ] → [ API Flask ] → [ Usuário / Cientista de Dados ]

yaml
Copiar
Editar

*(Você pode substituir por uma imagem de diagrama quando fizer.)*

---

## 🌍 Deploy

*(Se fizer deploy, insira aqui o link do Render ou Heroku)*

---

## 👨‍💻 Autor

- **Nome:** John Robert  
- **GitHub:** [johnrobert-oli](https://github.com/johnrobert-oli)

