from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Lê o CSV ao iniciar
df = pd.read_csv('data/books.csv')

@app.route('/')
def home():
    return "API de Livros funcionando!"

@app.route('/api/v1/books', methods=['GET'])
def get_books():
    books = df.to_dict(orient='records')
    return jsonify(books)

@app.route('/api/v1/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    if 0 <= book_id < len(df):
        book = df.iloc[book_id].to_dict()
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/api/v1/categories', methods=['GET'])
def get_categories():
    categories = df['category'].unique().tolist()
    return jsonify(categories)

@app.route('/api/v1/books/search', methods=['GET'])
def search_books():
    title = request.args.get('title', '').lower()
    category = request.args.get('category', '').lower()
    filtered = df

    if title:
        filtered = filtered[filtered['title'].str.lower().str.contains(title)]
    if category:
        filtered = filtered[filtered['category'].str.lower() == category]

    return jsonify(filtered.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
