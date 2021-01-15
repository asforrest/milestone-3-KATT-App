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


@app.route("/get_activities")
def get_activities():
    activities = list(mongo.db.activities.find())
    return render_template("activities.html", activities=activities)

# The code for user registration and sessions was adpated 
# from the User Authentication lessons @ Code Institute
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            flash("You are already registered, please log in with your email address and password")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email")
        flash("Registration Successful")
        return redirect(url_for('profile', email=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("email")
                    flash("Welcome, {}".format(
                        request.form.get("email")))
                    return redirect(url_for(
                        'profile', email=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # Grab session use's email from the db
    user = mongo.db.users.find_one(
         {"email": session["user"]})
    if session["user"]:
        return render_template("profile.html", user=user)

    return redirect(url_for("login"))



@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    activities = mongo.db.activities.find()
    return render_template("dashboard.html", activities=activities)


@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():
    if request.method == "POST":
        activity = {
            "date": request.form.get("date"),
            "activity_name": request.form.get("category_name"),
            "start_time": request.form.get("start_time"),
            "end_time": request.form.get("end_time"),
            "user_id": session["user"],
            "duration": "test_duration"
        }
        mongo.db.activities.insert_one(activity)
        flash("Activity added successfully")
        return redirect(url_for("get_activities"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_activity.html", categories=categories)


@app.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    activity = mongo.db.activity.find_one({"_id": ObjectId()})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_activity.html", activity = activity, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# Stopwatch code has been adapted from a tuturiol by Codegnan
# Source: https://www.youtube.com/watch?v=ekOeCnCSyUc
import time
def time_convert(secs):
    mins = secs // 60
    secs = secs % 60
    hours = mins // 60
    min = mins % 60
    print("Duration = {0}:{1}:{2}".format(int(hours),int(mins),int(secs)))
input("Press Enter to start")
start_time = time.time()
try:
    hours = 0
    while True:
        for minutes in range(0, 60):
            for seconds in range(0, 60):
                time.sleep(1)
                print(hours, ":", minutes, ":", seconds+1)
except KeyboardInterrupt:
    end_time = time.time()
    time_duration = end_time - start_time
    time_convert(time_duration)


from datetime import datetime

def run():
    current_time = datetime.now()
    diff = current_time - start_time
    txt.var.set('%d.%02d' % (diff.seconds,diff.microseconds//10000))

    if running:
        root.after(20,run) #to reschedule after 20ms


def start():
    global running
    global start_time

    if not running:
        running = True
        start_time = datetime.now()
        root.after(10,run)

def stop():
    global running
    running = Flase