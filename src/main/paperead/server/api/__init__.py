from .. import app
from paperead import __version__

from flask import jsonify


@app.route("/api/")
@app.route("/api/index.json")
def apiinfo():
    return jsonify({
        "version": __version__
    })
