from .. import app
from paperead import __version__

from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.route("/")
@api.route("/index.json")
def apiinfo():
    return jsonify({
        "version": __version__
    })


def build():
    from .materials import materials
    from .notes import notes
    
    api.register_blueprint(materials, url_prefix="/materials")
    api.register_blueprint(notes, url_prefix="/materials")
    return api