from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def login():
    if "username" in session:
        return "Logged in as %s" % session["username"]
    else:
        return "<form action='login' method='post'>" \
               "<input type='text' name='username'/>" \
               "<input type='password' name='password'/>" \
               "<input type='submit' value='login'/>" \
               "</form>"


@app.route("/login", methods=["POST"])
def do_login():
    if request.form["username"] == "wgj" and request.form["password"] == "123456":
        session["username"] = request.form["username"]
        return redirect(url_for("login"))
    else:
        return "login failure <a href='/'>back</a>"


app.secret_key = "1231"
app.run()
