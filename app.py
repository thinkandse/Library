from flask import Flask ,render_template, request, redirect, url_for, send_from_directory


app = Flask(__name__)

books = [
    {"id": 1, "title": "アナと雪の女王 (日本語)", "author": "ヂズニ", "genre": "冒険, ミュージカル", "description":"", "image":"https://th.bing.com/th/id/OIP.BD9qRMRQWSA2uj34mgVGfwHaHa"}, 
    {"id": 2, "title": "Advanced English Learner's Dictionary", "author": "Merriam-Webster", "genre": "", "description":"", "image":"https://th.bing.com/th/id/OIP.iGoDRhdVrpPWSnJvcgdAoQHaHa?rs=1&pid=ImgDetMain"},
    {"id": 3, "title": "A Philosophy of software design", "author": "", "genre": "", "description":"", "image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1531857377i/39996759.jpg"},
    {"id": 4, "title": "Encanto!", "author": "", "genre": "", "description":"", "image":"https://th.bing.com/th/id/OIP.hohw4_0x47Tj_CluLcQRlgHaLH?rs=1&pid=ImgDetMain"},
    {"id": 5, "title": "冰雪奇缘二 !", "author": "迪士尼", "genre": "Adventure, Musical", "description":"", "image":"https://th.bing.com/th/id/OIP.L8K42P_ChSjrF9eNfd_vFQHaKl?rs=1&pid=ImgDetMain"},
    {"id": 6, "title": "Skycircus", "author": "Peter Bunzl", "genre": "Children's Fiction", "description":"Enter a world of circus and adventure with Skycircus, the third book in the Cogheart series.", "image":"https://th.bing.com/th/id/OIP.UKHZ9qBje0mGFJby5aaJegHaLR?rs=1&pid=ImgDetMain"}, 
    
]

@app.route("/")
def listBook():
    return render_template("index.html",books = books)

booknumber = 7
@app.route("/add", methods = ["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    genre = request.form.get("genre")
    description = request.form.get("description")
    image = request.form.get("image")
    if title:
        new_id = len(books) + 1
        books.append({"id": new_id, "title": title, "author": author, "genre": genre, "description": description, "image": image})

    return redirect(url_for("listBook"))

"""@app.route("/book/<book_id>")
def specific_book(book_id):
    return send_from_directory("static/books/", f"{book_id}.html")"""

@app.route("/borrow/<int:book_id>")
def borrow_book(book_id):
    '''book = books.pop(book_id)
    return f"{book} has been borrowed"'''
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        books.remove(book)
        
    else:
        return "Book not found"
    return redirect(url_for("listBook"))

@app.route("/remove/<int:book_id>")
def remove_book(book_id):
    '''books.pop(book_id)
    return redirect(url_for("listBook"))'''
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        books.remove(book)
    return redirect(url_for("listBook"))

@app.route("/book/<int:book_id>")
def show_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return render_template("book_details.html", book = book)
    else:
        return "Book not found"

app.run(debug = True)