from flask import Flask ,render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

books = {
    "book1": "skycircus", #key : value
    "book2":"Encanto",
    "book3":"philosophysoftwaredesign",
    "book4":"dictionary",
    "book5":"アナと雪の女王 (日本語)",
    "book6":"冰雪奇缘二"
 
}

yahlist = 9
sutoring = "sutoring"
numbers = [1,2,3,4,5,6,7,8,9]
total = sum(numbers)



@app.route("/")
def listBook():
    return render_template("listBook.html",books = books)

@app.route("/show")
def page1():
    return render_template("index.html")#, gftjhk = yahlist, sutorings = sutoring, numbers = numbers, total = total)
    


    



booknumber = 7
@app.route("/add", methods = ["POST"])
def add_book():
    global booknumber
    z = request.form["b"]
    books[f"book{booknumber}"] = z
    booknumber += 1
    return redirect(url_for("listBook"))

@app.route("/book/<book_id>")
def specific_book(book_id):
    return send_from_directory("static/books/", f"{book_id}.html")




app.run(debug = True)