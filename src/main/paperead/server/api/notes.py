from dataclasses import asdict

from dateutil.parser import parse
from flask import abort, json, jsonify, request, send_from_directory

from paperead.repository.notes import Note, NoteMetadata

from paperead.env import env
from . import app


@app.route("/api/materials/<id>/notes/")
@app.route("/api/materials/<id>/notes/index.json")
def allNote(id: str):
    if id not in env.repo:
        abort(404)
    material = env.repo[id]
    return jsonify([item for item in material.notes])


@app.route("/api/materials/<id>/notes/<nid>/", methods=["GET"])
@app.route("/api/materials/<id>/notes/<nid>/index.json", methods=["GET"])
def getNote(id: str, nid: str):
    if id not in env.repo:
        abort(404)
    material = env.repo[id]
    if nid not in material.notes:
        abort(404)
    item = material.notes[nid]
    return jsonify(item)


@app.route("/api/materials/<id>/notes/<nid>/", methods=["DELETE"])
def deleteNote(id: str, nid: str):
    if id not in env.repo:
        abort(404)
    material = env.repo[id]
    if nid not in material.notes:
        abort(404)
    del material.notes[id]
    return id


@app.route("/api/materials/<id>/notes/", methods=["POST"])
def updateNote(id: str):
    if id not in env.repo:
        abort(404)

    data: dict = request.get_json()
    metadata = data.pop("metadata")
    metadata["creation"] = parse(metadata["creation"])          # isoformat
    metadata["modification"] = parse(metadata["modification"])  # isoformat
    metaobj = NoteMetadata(**metadata)
    obj = Note(metaobj, **data)

    material = env.repo[id]
    material.notes.update(obj)
    return obj.id
