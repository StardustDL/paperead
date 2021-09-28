from .. import app


@app.route("/api")
def hello_world():
    return "<p>Hello, World!</p>"
