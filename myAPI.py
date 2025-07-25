from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial list of books (each book is a dictionary with key-value pairs)
books = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 3, "title": "Sapiens", "author": "Yuval Noah Harari"}
]

@app.route('/')
def home():
    return "My name is Amartya"

# Route to GET all books or POST a new book
@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        return jsonify(books)

    if request.method == 'POST':
        new_book = request.json  # Get JSON data sent from client
        books.append(new_book)
        return jsonify(new_book), 201

# Route to GET, UPDATE, or DELETE a specific book by its ID
@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    # Find the book with matching ID
    book = next((b for b in books if b['id'] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'GET':
        return jsonify(book)

    elif request.method == 'PUT':
        book.update(request.json)
        return jsonify(book)

    elif request.method == 'DELETE':
        books.remove(book)
        return jsonify({"message": "Book deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
