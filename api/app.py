from flask import Flask, jsonify, request
import pandas as pd
import os
from flasgger import Swagger

app = Flask(__name__)

# Swagger básico (abre em /apidocs)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Books API",
        "version": "1.0.0",
        "description": "API do Tech Challenge para consultar livros do Books to Scrape."
    },
    "basePath": "/"
})

# tenta abrir o arquivo com os livros
CSV_PATHS = [
    "data/books.csv",
    "./data/books.csv",
]

df = None
for path in CSV_PATHS:
    if os.path.exists(path):
        df = pd.read_csv(path)
        break

# se não encontrar, cria um vazio só pra não travar
if df is None:
    df = pd.DataFrame(columns=["title", "price", "rating", "availability", "category", "image_url"])

# garante que todas as colunas existem
expected_cols = {"title", "price", "rating", "availability", "category", "image_url"}
for col in expected_cols:
    if col not in df.columns:
        df[col] = pd.Series(dtype="object")

# troca valores estranhos (NaN) por None
df = df.where(pd.notnull(df), None)


# página inicial
@app.route("/", methods=["GET"])
def home():
    """
    Home
    ---
    tags: [Geral]
    responses:
      200:
        description: Mensagem simples confirmando que a API está no ar.
    """
    return "API de Livros funcionando!", 200


# rota pra ver se a API está no ar
@app.route("/api/v1/health", methods=["GET"])
def health():
    """
    Health check
    ---
    tags: [Geral]
    responses:
      200:
        description: Status OK
        schema:
          type: object
          properties:
            status:
              type: string
              example: ok
    """
    return jsonify({"status": "ok"}), 200


# rota que mostra todas as rotas disponíveis (apoio)
@app.route("/__routes", methods=["GET"])
def routes():
    """
    Lista de rotas (apoio)
    ---
    tags: [Geral]
    responses:
      200:
        description: Lista todas as rotas registradas (texto simples).
    """
    return "\n".join(sorted(str(r) for r in app.url_map.iter_rules())), 200, {"Content-Type": "text/plain"}


# retorna todos os livros
@app.route("/api/v1/books", methods=["GET"])
def get_books():
    """
    Lista todos os livros
    ---
    tags: [Livros]
    responses:
      200:
        description: Lista de livros
        schema:
          type: array
          items:
            type: object
            properties:
              title: {type: string}
              price: {type: string}
              rating: {type: string}
              availability: {type: string}
              category: {type: string}
              image_url: {type: string}
    """
    books = df.to_dict(orient="records")
    return jsonify(books), 200


# retorna um livro pelo id
@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id: int):
    """
    Livro por ID
    ---
    tags: [Livros]
    parameters:
      - name: book_id
        in: path
        required: true
        type: integer
        description: Índice do livro (0 baseado)
    responses:
      200:
        description: Livro encontrado
        schema:
          type: object
      404:
        description: Não encontrado
        schema:
          type: object
          properties:
            error: {type: string}
    """
    if 0 <= book_id < len(df):
        book = df.iloc[book_id].to_dict()
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


# retorna todas as categorias
@app.route("/api/v1/categories", methods=["GET"])
def get_categories():
    """
    Lista categorias
    ---
    tags: [Livros]
    responses:
      200:
        description: Lista de categorias (sem repetição)
        schema:
          type: array
          items: {type: string}
    """
    categories = sorted([c for c in set(df["category"].tolist()) if c is not None])
    return jsonify(categories), 200


# busca livros pelo título e/ou categoria
@app.route("/api/v1/books/search", methods=["GET"])
def search_books():
    """
    Busca livros
    ---
    tags: [Livros]
    parameters:
      - name: title
        in: query
        type: string
        required: false
        description: Parte do título (case-insensitive)
      - name: category
        in: query
        type: string
        required: false
        description: Categoria exata (case-insensitive)
    responses:
      200:
        description: Resultado da busca
        schema:
          type: array
          items:
            type: object
    """
    title = (request.args.get("title") or "").strip().lower()
    category = (request.args.get("category") or "").strip().lower()
    filtered = df

    if title:
        filtered = filtered[filtered["title"].fillna("").str.lower().str.contains(title)]
    if category:
        filtered = filtered[filtered["category"].fillna("").str.lower() == category]

    return jsonify(filtered.to_dict(orient="records")), 200


# executa localmente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
