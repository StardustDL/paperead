from dataclasses import asdict

from dateutil.parser import parse
from flask import abort, json, jsonify, request, send_from_directory, Blueprint

from paperead.repository.notes import Note
from . import buildDocument

from paperead.env import env


notes = Blueprint("notes", __name__)


@notes.route("/<id>/notes/")
@notes.route("/<id>/notes/index.json")
def allNote(id: str):
    if id not in env.repo:
        abort(404)
    material = env.repo[id]
    return jsonify([item for item in material.notes])


@notes.route("/<id>/notes/<nid>/", methods=["GET"])
@notes.route("/<id>/notes/<nid>/index.json", methods=["GET"])
def getNote(id: str, nid: str):
    if id not in env.repo:
        abort(404)
    material = env.repo[id]
    if nid not in material.notes:
        abort(404)
    item = material.notes[nid]
    return jsonify(item)


@notes.route("/<id>/notes/<nid>/", methods=["DELETE"])
def deleteNote(id: str, nid: str):
    if id not in env.repo:
        abort(404)
    material = env.repo[id]
    if nid not in material.notes:
        abort(404)
    del material.notes[id]
    return id


@notes.route("/<id>/notes/", methods=["POST"])
def updateNote(id: str):
    if id not in env.repo:
        abort(404)

    obj = buildDocument(Note, request.get_json())

    material = env.repo[id]
    material.notes.update(obj)
    return obj.id
