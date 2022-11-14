from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
import datetime
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_mail import Mail, Message

# an instance of flask
application = Flask(__name__)


# # path
# basedir = os.path.abspath(os.path.dirname(__file__))
# # initialise the database with sqlalchemy
# # mysql://username:password@host:port/database_name
# application.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "mysql://root:OLUDEdavid1995@localhost:3306/bio-medic"
# application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# flask mail
application.config["DEBUG"] = True
application.config["TESTING"] = False
application.config["MAIL_SERVER"] = "smtp.gmail.com"
application.config["MAIL_PORT"] = 587
application.config["MAIL_USERNAME"] = "odavidolumide@gmail.com"
application.config["MAIL_PASSWORD"] = ""
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_ASCII_ATTACHMENTS"] = False
application.config["MAIL_DEFAULT_SENDER"] = None


# db = SQLAlchemy(application)
application.config["GOOGLEMAPS_KEY"] = "8JZ7i18MjFuM35dJHq70n3Hx4"

# Initialize the extension
GoogleMaps(application)

# Flask Mail
mail = Mail(application)


@application.route("/map")
def mapview():

    return render_template("example.html")


# routes
@application.route("/")
@application.route("/home")
def home():
    time = datetime.datetime.utcnow()

    return render_template("home.html", time=time)


@application.route("/about")
def about():
    return render_template("about.html")


@application.route("/service")
def service():
    return render_template("service.html")


@application.route("/contact")
def contact():
    time = datetime.datetime.utcnow()
    return render_template("contact.html", time=time)


if __name__ == "__main__":
    application.run(debug=True)
