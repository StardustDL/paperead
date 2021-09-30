from dataclasses import asdict

from dateutil.parser import parse
from flask import abort, json, jsonify, request, send_from_directory

from paperead.repository.materials import Material, MaterialMetadata

from paperead.env import env
from . import app


@app.route("/api/materials/")
@app.route("/api/materials/index.json")
def allMaterial():
    return jsonify([id for id in env.repo])


@app.route("/api/materials/<id>/", methods=["GET"])
@app.route("/api/materials/<id>/index.json", methods=["GET"])
def getMaterial(id: str):
    if id not in env.repo:
        abort(404)
    item = env.repo[id]

    return jsonify(item)


@app.route("/api/materials/<id>/", methods=["DELETE"])
def deleteMaterial(id: str):
    if id not in env.repo:
        abort(404)
    del env.repo[id]
    return id


@app.route("/api/materials/", methods=["POST"])
def updateMaterial():
    data: dict = request.get_json()
    metadata = data.pop("metadata")
    metadata["creation"] = parse(metadata["creation"])          # isoformat
    metadata["modification"] = parse(metadata["modification"])  # isoformat

    metaobj = MaterialMetadata(**metadata)
    obj = Material(metaobj, **data)

    env.repo.update(obj)
    return obj.id


@app.route("/api/materials/<id>/assets/<path:path>", methods=["GET"])
def assets(id: str, path: str):
    if id not in env.repo:
        abort(404)
    item = env.repo[id]
    return send_from_directory(item.assets, path)
