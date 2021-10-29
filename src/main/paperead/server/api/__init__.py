from dataclasses import asdict
from typing import Callable, Type

from paperead.repository import DocumentMetadata
from paperead import __version__
from paperead.env import env

from flask import Blueprint, jsonify
from dateutil.parser import parse

api = Blueprint("api", __name__)


def buildDocument(type: Type, data: dict):
    metadata = data.pop("metadata")
    metadata["creation"] = parse(metadata["creation"])          # isoformat
    metadata["modification"] = parse(metadata["modification"])  # isoformat

    metaobj = DocumentMetadata(**metadata)
    return type(metaobj, **data)


@api.route("/")
@api.route("/index.json")
def apiinfo():
    return jsonify({
        "version": __version__,
        "site": asdict(env.siteConfig)
    })


def build():
    from .materials import materials
    from .notes import notes

    api.register_blueprint(materials, url_prefix="/materials")
    api.register_blueprint(notes, url_prefix="/materials")
    return api
