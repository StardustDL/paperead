import pathlib

from flask import send_file, send_from_directory

from . import app

wwwroot = pathlib.Path(__file__).parent.joinpath("wwwroot")


@app.route("/", methods=["GET"])
@app.route("/<path:path>", methods=["GET"])
def wwwrootFiles(path: str = "index.html"):
    return send_from_directory(wwwroot, path)


@app.errorhandler(404)
def pageNotFound(error):
    return send_file(wwwroot.joinpath("index.html"))
