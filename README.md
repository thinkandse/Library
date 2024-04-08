# Library
<h2>This Library contains movies + books to borrow</h2>
<h3>⚠UNPOLISHED!</h3>

- app.route("/") = http://127.0.0.1:5000/
- for attribute in the label tag is used to bind the label and input box together so if click on the label, input box will be clicked
- in app.py, whatever you put inside "get" method should be the same as the name of the input box so the name and the get method should contain the same thing
- if title: means we are checking that user entered a title in the input box or not and if user didn't add any title, we will not that book
- len(books) + 1 is used to find the id of the new book because first we are finding the number of books which are already present in the list so let's assume we have 6 books in the books list
  those books will have ids from 1 till six so the new book will have id of 7 that's why we added 1
- return redirect(url_for("listBook")) redirect is used to get redirected to a new page and here, the new page is index.html because listbook function is rendering index.html
- return render_template("index.html",<strong>books = books</strong>) books = books means we are sending the books list which contains all the books from the backend to the frontend so that index.html can show that
- @app.route("/borrow/<int:book_id>") borrow means going to the borrow page which actually contains nothing so it will give you an error, but, if you put borrow/(id) it will remove that particular book from the books list because that's been borrowed and to make the URL as borrow/1 we need to write "/borrow/<int:book_id>" book_id is a variable
