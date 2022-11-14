from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
import datetime
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_mail import Mail, Message

# an instance of flask
app = Flask(__name__)


# # path
# basedir = os.path.abspath(os.path.dirname(__file__))
# # initialise the database with sqlalchemy
# # mysql://username:password@host:port/database_name
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "mysql://root:OLUDEdavid1995@localhost:3306/bio-medic"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# flask mail
app.config["DEBUG"] = True
app.config["TESTING"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "odavidolumide@gmail.com"
app.config["MAIL_PASSWORD"] = ""
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_ASCII_ATTACHMENTS"] = False
app.config["MAIL_DEFAULT_SENDER"] = None


# db = SQLAlchemy(app)
app.config["GOOGLEMAPS_KEY"] = "8JZ7i18MjFuM35dJHq70n3Hx4"

# Initialize the extension
GoogleMaps(app)

# Flask Mail
mail = Mail(app)


@app.route("/map")
def mapview():

    return render_template("example.html")


# routes
@app.route("/")
@app.route("/home")
def home():
    time = datetime.datetime.utcnow()

    return render_template("home.html", time=time)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/contact")
def contact():
    time = datetime.datetime.utcnow()
    return render_template("contact.html", time=time)


if __name__ == "__main__":
    app.run(debug=True)
