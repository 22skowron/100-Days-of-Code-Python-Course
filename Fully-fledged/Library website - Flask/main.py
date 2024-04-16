from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import IntegrityError

############################################################################################
    # DATABASE CONFIG

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

    # APP CONFIG:
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

    # BOOK ENTITY:
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book: id - {self.id}, title - {self.title}>'

    # CREATE TABLE SCHEMA IN DATABASE:
with app.app_context():
    db.create_all()


############################################################################################
    # WEBPAGES

@app.route('/')
def home():
    with app.app_context():
        books = db.session.execute(db.select(Book)).scalars().all()

        for book in books:
            if "0" == str(book.rating).split(".")[1]:
                book.rating = int(book.rating)

    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form.get('book_name'),
                author=request.form.get('book_author'),
                rating=request.form.get('book_rating')
            )
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get("id")

    if request.method == "GET":
        with app.app_context():
            book = db.session.get(Book, book_id)
        return render_template("edit_rating.html", book=book)

    if request.method == "POST":
        with app.app_context():
            new_rating = request.form.get("new_rating")
            print(f"Editing the book with the id: {book_id}, new rating: {new_rating}.")
            book_to_edit = db.session.get(Book, book_id)
            book_to_edit.rating = new_rating
            db.session.commit()
        return redirect(url_for('home'))


@app.route("/delete")
def delete():
    with app.app_context():
        book_id = request.args.get("id")
        book_to_delete = db.session.get(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


############################################################################################
    # RUN APP

if __name__ == "__main__":
    app.run(debug=True)

