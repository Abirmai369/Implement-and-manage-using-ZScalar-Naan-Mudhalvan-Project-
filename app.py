
from flask import Flask, render_template, request, redirect, session
from database import validate_user
from policy_engine import check_access

app = Flask(__name__)
app.secret_key = "ztna_secret_key"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if validate_user(username,password):
            if check_access(username):
                session["user"]=username
                return redirect("/dashboard")
            else:
                return "Access Denied by ZTNA Policy"
        else:
            return "Invalid Credentials"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html",user=session["user"])
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
