from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), unique=True, nullable=False)
        rating = db.Column(db.Float, nullable=False)
    
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html", books=Book.query.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        new_book = Book(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit() 
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/editid=<int:index>', methods=["GET", "POST"])
def edit(index):
    inf = Book.query.get(index)
    if request.method == "POST":
        book_rating = request.form
        new_rate = book_rating["new_rating"] 
        inf.rating = new_rate
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", data=inf)
    
@app.route('/delete')
def remove():
    del_id = request.args.get('index')
    del_book = Book.query.get(del_id)
    db.session.delete(del_book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)