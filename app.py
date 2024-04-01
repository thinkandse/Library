from flask import Flask ,render_template, request, redirect, url_for, send_from_directory


app = Flask(__name__)

books = [
    {"id": 1, "title": "アナと雪の女王 (日本語)", "author": "ヂズニ", "genre": "", "description":""}, 
    {"id": 2, "title": "Advanced English Learner's Dictionary", "author": "Merriam-Webster", "genre": "", "description":""},
    {"id": 3, "title": "アナと雪の女王 (日本語)", "author": "", "genre": "", "description":""},
    {"id": 4, "title": "アナと雪の女王 (日本語)", "author": "", "genre": "", "description":""},
    {"id": 5, "title": "アナと雪の女王 (日本語)", "author": "", "genre": "", "description":""},
    {"id": 6, "title": "Skycircus", "author": "Peter Bunzl", "genre": "Children's Fiction", "description":"Enter a world of circus and adventure with Skycircus, the third book in the Cogheart series."}, 
    
]



yahlist = 9
sutoring = "sutoring"
numbers = [1,2,3,4,5,6,7,8,9]
total = sum(numbers)





@app.route("/")
def listBook():
    return render_template("index.html",books = books)

booknumber = 7
@app.route("/add", methods = ["POST"])
def add_book():
    global booknumber
    title = request.form["b"]
    books[f"book{booknumber}"] = title
    booknumber += 1
    return redirect(url_for("listBook"))

@app.route("/book/<book_id>")
def specific_book(book_id):
    return send_from_directory("static/books/", f"{book_id}.html")

@app.route("/borrow/<book_id>")
def borrow_book(book_id):
    book = books.pop(book_id)
    return f"{book} has been borrowed"

@app.route("/remove/<book_id>")
def remove_book(book_id):
    books.pop(book_id)
    return redirect(url_for("listBook"))


app.run(debug = True)