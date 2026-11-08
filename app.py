from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> PRN : 123456 </h1> <h2>Student Name: sarfaraz</h2>"

app.run(host="0.0.0.0", port=5000)
