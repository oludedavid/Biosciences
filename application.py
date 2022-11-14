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
