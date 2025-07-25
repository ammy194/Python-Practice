from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    books = [
        {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
        {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho"},
        {"id": 3, "title": "Sapiens", "author": "Yuval Noah Harari"}
    ]

    # Define user_data first
    user_data = {
        "user_id": user_id,
        "books": books
    }

    # Get extra value from URL like ?extra=something
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

if __name__ == "__main__":
    app.run(debug=True)
