from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)



class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
        
            
@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    all_cafes = {"cafes": []}
    for index in range(len(cafes)):
        all_cafes["cafes"].append({
            "id": cafes[index].id,
            "name": cafes[index].name,
            "map_url": cafes[index].map_url,
            "img_url": cafes[index].img_url,
            "location": cafes[index].location,
            "seats":cafes[index].seats,
            "has_toilet": cafes[index].has_toilet,
            "has_wifi": cafes[index].has_wifi,
            "has_sockets": cafes[index].has_sockets,
            "can_take_calls": cafes[index].can_take_calls,
            "coffee_price": cafes[index].coffee_price,
        })

    return jsonify(all_cafes)


@app.route("/search")
def search():
    loc = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=loc).all()
    all_cafes = {"cafes": []}
    for index in range(len(cafes)):
        all_cafes["cafes"].append({
            "id": cafes[index].id,
            "name": cafes[index].name,
            "map_url": cafes[index].map_url,
            "img_url": cafes[index].img_url,
            "location": cafes[index].location,
            "seats":cafes[index].seats,
            "has_toilet": cafes[index].has_toilet,
            "has_wifi": cafes[index].has_wifi,
            "has_sockets": cafes[index].has_sockets,
            "can_take_calls": cafes[index].can_take_calls,
            "coffee_price": cafes[index].coffee_price,
        })
    try:
        if loc in all_cafes["cafes"][0]["location"] == loc:
            return jsonify(all_cafes)
    except: 
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:id>", methods=["PATCH"])
def update(id):
    new_price = request.args.get("new_price")
    try:
        cafe = Cafe.query.get(id)
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price"})
    except:
        return jsonify(response={"error": "Sorry a cafe with that id was not found in the database"})


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = Cafe.query.get(cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully delete the cafe"})
        except:
            return jsonify(response={"error": "Sorry a cafe with that id was not found in the database"})
    else:
        return jsonify(response={"error": "Sorry, wrong api-key"})
    


if __name__ == '__main__':
    app.run(debug=True)

#docs 
#https://documenter.getpostman.com/view/26243735/2s93JqSjrn    