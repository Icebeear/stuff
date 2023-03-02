from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from login import LoginForm
import requests
import smtplib

data = requests.get(url="https://api.npoint.io/4cedc647e52fc72c2543").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route("/")
def main():
    return render_template("index.html", all_posts=data)

@app.route("/index.html")
def index():
    return render_template("index.html", all_posts=data)

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
            data = request.form
            send_mail(name=data["fname"], email=data["email"], phone=data["phone"], message=data["message"])
            return render_template("contact.html", title="Successfully sent your message")
    else:
        return render_template("contact.html", title="Contact Me")
        

@app.route("/post<int:index>.html")
def post(index):
    return render_template("post.html", post=data[index - 1])

def send_mail(name, email, phone, message):
     sms = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
     sms = sms.encode('ascii', 'ignore').decode('ascii')
     with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
                connection.starttls()
                connection.login(user="example", password="example")
                connection.sendmail(
                "example", "example", f"Subject:{'New Message'}\n\n{sms}"
                )

@app.route("/login.html", methods=["GET", "POST"])
def login():
        login_form = LoginForm()
        email_error = ""
        password_error = ""
        if login_form.is_submitted():
           if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
                 return render_template("success.html")
           else:
                 return render_template("denied.html")
        
        return render_template("login.html", form=login_form)



        #     if "@" not in login_form.email.data or "." not in login_form.email.data:
        #         email_error = "Invalid email adress"
        #     else:
        #         email_error = ""
        #     if len(login_form.password.data) < 8:
        #         password_error = "Field must be at least 8 characters long"
        #     else:
        #         password_error = ""
        # return render_template("login.html", form=login_form, email_error=email_error, password_error=password_error)



if __name__ == "__main__":
    app.run(debug=True)