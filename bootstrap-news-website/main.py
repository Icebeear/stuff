from flask import Flask, render_template, request
import requests
import smtplib

data = requests.get(url="https://api.npoint.io/4cedc647e52fc72c2543").json()

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)