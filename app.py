import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/balegro")
def balegro():
    return render_template("balegro.html")


@app.route("/sunrise")
def sunrise():
    return render_template("sunrise.html")


@app.route("/offset")
def offset():
    return render_template("offset.html")


@app.route("/dimma")
def dimma():
    return render_template("dimma.html")


@app.route("/offspringAI")
def offspringAI():
    return render_template("offspringAI.html")


@app.route("/offspringJR")
def offspringJR():
    return render_template("offspringJR.html")


@app.route("/offspringSZ")
def offspringSZ():
    return render_template("offspringSZ.html")


@app.route("/addOffspring")
def addOffspring():
    return render_template("addOffspring.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/logOut")
def logOut():
    return render_template("logOut.html")


@app.route("/logIn")
def logIn():
    return render_template("logIn.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
