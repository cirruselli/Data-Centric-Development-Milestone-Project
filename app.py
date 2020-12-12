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
    stallions = mongo.db.stallions.find()  # Get all Stallions in db.
    # Total Number of offsprings to devide by.
    totNumberOffspring = mongo.db.offsprings.find().count()
    # offsprings = mongo.db.offsprings.find()  # Get all Offspring in db.
    horsesStat = []  # Init an empty array to save Stallions
    for horse in stallions:
        ownOffspring = mongo.db.offsprings.find(
            {"father": horse["name"]}).count()
        procent = ownOffspring / totNumberOffspring
        # Save stallion with it's procent of tot.Offsprings in
        # an array that's sent to the webfront.
        horsesStat.append(
            [horse["name"].capitalize(), round(procent * 100, 1)])

    return render_template("home.html", horsesStat=horsesStat)


@app.route("/balegro")
def balegro():
    stallion = mongo.db.stallions.find_one({"name": "balegro"})
    offspring = mongo.db.offsprings.find(
        {"father": "balegro"}).count()
    return render_template(
        "balegro.html", stallion=stallion, offspring=offspring)


@app.route("/sunrise")
def sunrise():
    stallion = mongo.db.stallions.find_one({"name": "sunrise"})
    offspring = mongo.db.offsprings.find(
        {"father": "sunrise"}).count()
    return render_template(
        "sunrise.html", stallion=stallion, offspring=offspring)


@app.route("/offset")
def offset():
    stallion = mongo.db.stallions.find_one({"name": "offset"})
    offspring = mongo.db.offsprings.find(
        {"father": "offset"}).count()
    return render_template(
        "offset.html", stallion=stallion, offspring=offspring)


@app.route("/dimma")
def dimma():
    stallion = mongo.db.stallions.find_one({"name": "dimma"})
    offspring = mongo.db.offsprings.find(
        {"father": "dimma"}).count()
    return render_template(
        "dimma.html", stallion=stallion, offspring=offspring)


@app.route("/offspringAI")
def offspringAI():
    offsprings = list(mongo.db.offsprings.find().sort("name", 1))

    return render_template(
        "offspringAI.html", offsprings=offsprings)


@app.route("/addOffspring", methods=["GET", "POST"])
def addOffspring():
    if request.method == "POST":
        offspring = {
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
        mongo.db.offsprings.insert_one(offspring)
        flash("Offspring successfully added")
        return redirect(url_for("addOffspring"))

    offsprings = mongo.db.offsprings.find().sort("name", 1)
    stallions = mongo.db.stallions.find().sort("name", 1)
    print(stallions)
    return render_template(
        "addOffspring.html", offsprings=offsprings, stallions=stallions)


@app.route("/editOffspring/<offspring_id>", methods=["GET", "POST"])
def editOffspring(offspring_id):
    if request.method == "POST":
        submit = {
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
        mongo.db.offsprings.update({"_id": ObjectId(offspring_id)}, submit)
        flash("Offspring successfully updated")
        return redirect(url_for("offspringAI"))

    offspring = mongo.db.offsprings.find_one(
        {"_id": ObjectId(offspring_id)})
    stallions = mongo.db.stallions.find().sort("name", 1)
    return render_template(
        "editOffspring.html", offspring=offspring, stallions=stallions)


@app.route("/deleteOffspring/<offspring_id>")
def deleteOffspring(offspring_id):
    mongo.db.offsprings.remove({"_id": ObjectId(offspring_id)})
    flash("Offspring successfully deleted")
    return redirect(url_for("offspringAI"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        offsprings = list(mongo.db.offsprings.find(
         {"$text": {"$search": query}}))
        return render_template("offspringAI.html", offsprings=offsprings)


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
        return redirect(url_for("home"))

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
                flash("Hello and welcome, {}".format(request.form.get(
                    "username")))
                return redirect(url_for("home"))
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
