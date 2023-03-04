from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import imdb
imdb = imdb.Cinemagoer()



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///movies.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)
Bootstrap(app)


class EditForm(FlaskForm):
    rating = StringField(label="Your Rating Ot of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="You Review", validators=[DataRequired()])
    done = SubmitField(label="Done", validators=[DataRequired()])

class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    add_button = SubmitField(label="Add Movie", validators=[DataRequired()])

with app.app_context():
    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        year = db.Column(db.Integer, nullable=False)
        description = db.Column(db.String, nullable=False)
        rating = db.Column(db.Float, nullable=False)
        ranking = db.Column(db.Integer, nullable=False)
        review = db.Column(db.String, nullable=False)
        img_url = db.Column(db.String, nullable=False)

    db.create_all()


def get_movies(movie):
    films = []
    movies = imdb.search_movie(movie)
    for x in range(len(movies)):
        movie = movies[x]
        m_id = movie.movieID
        info = imdb.get_movie(m_id).data
        films.append(info)
    return films

    

@app.route("/", methods=["GET", "POST"])
def home():
    movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    for x in range(len(movies)):
        movies[x].ranking = x + 1 
    return render_template("index.html", data=movies)


@app.route("/edit/<int:id><string:title>", methods=["GET", "POST"])
def edit(id, title):
    edit_form = EditForm()
    if edit_form.is_submitted():
        data = request.form
        movie = Movie.query.get(id)
        movie.rating = data["rating"]
        movie.review = data["review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, title=title)

@app.route("/<int:id>")
def remove(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.is_submitted():
        title = request.form["title"]
        return render_template("select.html", movies=get_movies(title))
    
    return render_template("add.html", form=add_form)

@app.route("/new_film<int:id>", methods=["GET", "POST"])
def new_film(id):
    data = imdb.get_movie(id).data
    new_movie = Movie(
        title=data["title"],
        year=data["year"],
        description=data["plot outline"],
        rating=data["rating"],
        ranking="none",
        review="none",
        img_url=data["cover url"]
    )

    db.session.add(new_movie)
    db.session.commit()
    movie = db.session.query(Movie).order_by(Movie.id.desc()).first()
    return redirect(url_for("edit", id=movie.id, title=movie.title))


if __name__ == '__main__':
    app.run(debug=True)