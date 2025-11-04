from flask import Flask, request
app = Flask(__name__)

@app.route("/")   # ✅ This will display the form
def home():
    return open("index.html").read()   # ✅ Loads your HTML file

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"].strip()
    fb = request.form["fb"].strip()

    if name == "" or fb == "":
        return "Error: Empty fields"
    if "<script" in name.lower() or "<script" in fb.lower():
        return "Error: Script tag not allowed"

    return "Feedback Received: " + name + " - " + fb

app.run()
