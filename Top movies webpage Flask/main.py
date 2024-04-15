from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import IntegrityError
from wtforms import StringField, SubmitField, IntegerField, FloatField, Form
from wtforms.validators import DataRequired, URL, NumberRange
from flask_wtf import FlaskForm
from dotenv import load_dotenv
import requests
import os


####################################################################################
    # SET UP THE APP

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
Bootstrap5(app)

####################################################################################
    # SET UP A DATABASE

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Table model
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(4000), unique=True)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(4000))
    img_url: Mapped[str] = mapped_column(String(400), unique=True)

    def __repr__(self):
        return f"<Movie: id - {self.id}, title - {self.title}, rating - {self.rating}.>"

# Create a table if not present yet
with app.app_context():
    db.create_all()

####################################################################################
# Insert some data to database:
# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()
#
# with app.app_context():
#     new_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

####################################################################################
    # FORMS

class AddMovie(FlaskForm):
    title = StringField(validators=[DataRequired()])
    year = IntegerField(validators=[DataRequired()])
    description = StringField(validators=[DataRequired()])
    rating = FloatField(validators=[DataRequired(), NumberRange(min=0, max=10)])
    ranking = IntegerField(validators=[DataRequired()])
    review = StringField(validators=[DataRequired()])
    img_url = StringField(label="Image URL", validators=[URL()])
    submit = SubmitField(label="Submit", render_kw={"class": "container text-center add"})


class EditRating(FlaskForm):
    new_rating = FloatField(label="Your rating (out of 10)", validators=[DataRequired(), NumberRange(min=0, max=10)])
    new_review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


####################################################################################
    # FUNCTIONS

def update_ratings():
    with app.app_context():
        movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()

        # Order movies by rating
        for movie in movies:
            movie.ranking = movies.index(movie) + 1
        db.session.commit()


####################################################################################
    # WEBPAGES

@app.route("/")
def home():
    with app.app_context():
        movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()

    return render_template("index.html", movies=movies)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    add_movie_form = AddMovie(formdata=request.form)
    print(add_movie_form.data)
    if add_movie_form.validate_on_submit():
        print("Form validated")
        try:
            with app.app_context():
                new_movie = Movie(
                    title=add_movie_form.title.data,
                    year=add_movie_form.year.data,
                    description=add_movie_form.description.data,
                    rating=add_movie_form.rating.data,
                    ranking=add_movie_form.ranking.data,
                    review=add_movie_form.review.data,
                    img_url=add_movie_form.img_url.data
                )
                db.session.add(new_movie)
                db.session.commit()
            update_ratings()
            print("Form successfully added.")
            return redirect(url_for('add_movie'))

        except IntegrityError:
            print("Error. Movie not added to a database since it is a duplicate"
                  " of another movie.")

    return render_template("add_movie.html", form=add_movie_form)


@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
        # Get movie id
    movie_edit_id = request.args.get("id")
    with app.app_context():
        movie_to_edit = db.session.get(Movie, movie_edit_id)

        # Form
    edit_rating_form = EditRating(formdata=request.form)

    if edit_rating_form.validate_on_submit():
        with app.app_context():
            movie_to_edit = db.session.get(Movie, movie_edit_id)
            movie_to_edit.rating = edit_rating_form.new_rating.data
            movie_to_edit.review = edit_rating_form.new_review.data
            db.session.commit()
        update_ratings()
        print("Rating and review successfully updated.")
        return redirect(url_for('home'))

    return render_template("edit.html", movie_to_edit=movie_to_edit, form=edit_rating_form)


@app.route("/delete")
def delete_movie():
    movie_delete_id = request.args.get('id')
    with app.app_context():
        movie_to_delete = db.session.get(Movie, movie_delete_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    update_ratings()
    return redirect(url_for('home'))

####################################################################################
    # RUN APP

if __name__ == '__main__':
    app.run(debug=False)
