from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
with app.app_context():
    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(100), unique=True)
        password = db.Column(db.String(100))
        name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form 
        new_user = User(email=data["email"],
                        password=generate_password_hash(data["password"], method='pbkdf2:sha256', salt_length=8),
                        name=data["name"],
                        )
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets"))
    
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        data = request.form
        login = data["email"]
        password = data["password"]

        try:
            user = User.query.filter_by(email=login).first()
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Wrong password")
                return redirect(url_for("login"))
        except:
            flash("Wrong email")
            return redirect(url_for("login"))
       
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory('static/files', filename, as_attachment=True)
    


if __name__ == "__main__":
    app.run(debug=True)
