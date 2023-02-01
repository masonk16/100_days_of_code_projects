from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


db = sqlite3.connect("books-collection.db")
cursor = db.cursor()



all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add")
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)

        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
