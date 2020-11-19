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
    stallion = mongo.db.stallions.find_one({"name": "Balegro"})
    return render_template("balegro.html", stallion=stallion)


@app.route("/sunrise")
def sunrise():
    stallion = mongo.db.stallions.find_one({"name": "sunrise"})
    return render_template("sunrise.html", stallion=stallion)


@app.route("/offset")
def offset():
    stallion = mongo.db.stallions.find_one({"name": "offset"})
    return render_template("offset.html", stallion=stallion)


@app.route("/dimma")
def dimma():
    stallion = mongo.db.stallions.find_one({"name": "dimma"})
    return render_template("dimma.html", stallion=stallion)


@app.route("/offspringAI")
def offspringAI():
    return render_template("offspringAI.html")


@app.route("/offspringJR")
def offspringJR():
    return render_template("offspringJR.html")


@app.route("/offspringSZ")
def offspringSZ():
    return render_template("offspringSZ.html")


@app.route("/addOffspring", methods=["GET", "POST"])
def addOffspring():
    if request.method == "POST":
        addOffspring = {
            "name": request.form.get("name"),
            "birth_year": request.form.get("birth_year"),
            "gender": request.form.get("gender"),
            "father": request.form.get("father"),
            "mother": request.form.get("mother"),
            "breed": request.form.get("breed"),
            "country": request.form.get("country"),
            "owner": request.form.get("owner"),
            "achievements": request.form.get("achievements"),
            "created_by": session["user"]
        }
        mongo.db.offsprings.insert_one(addOffspring)
        flash("Offspring successfully added")
        return redirect(url_for("addOffspring"))

    offspring = mongo.db.offsprings.find().sort("name", 1)
    return render_template("addOffspring.html", offspring=offspring)


@app.route("/search")
def search():
    return render_template("search.html")


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


@app.route("/logIn", methods=["GET", "POST"])
def logIn():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello and welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("logIn"))

        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("logIn"))

    return render_template("logIn.html")


@app.route("/logOut")
def logOut():
    flash("You have been logged out")
    session.pop("user")
    return render_template("logOut.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
