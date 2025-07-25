from Flask import flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 3, "title": "Sapiens", "author": "Yuval Noah Harari"}
]

@app.route('/')
def home():
    return "My name is Amartya"

@app.route('/books', methods = ['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        return jsonify(books)
    
    if request.method == 'POST':
        new_book = request.json
        books.append(new_book)
        return jsonify(new_book), 201
    
@app.route('/books/<int: book_id>',methods = ['GET', 'PUT', 'DELETE'])
def handle_books(book_id):
    book = next((b for b in book if b['id'] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    




    

        


