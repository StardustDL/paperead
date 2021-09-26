from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api")
def hello_world():
    return "<p>Hello, World!</p>"
