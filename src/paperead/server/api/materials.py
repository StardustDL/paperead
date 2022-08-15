from dataclasses import asdict

from flask import abort, json, jsonify, request, send_from_directory, Blueprint

from paperead.env import env
from paperead.repository.materials import Material
from . import buildDocument


materials = Blueprint("materials", __name__)


@materials.route("/")
@materials.route("/index.json")
def allMaterial():
    return jsonify([id for id in env.repo])


@materials.route("/<id>/", methods=["GET"])
@materials.route("/<id>/index.json", methods=["GET"])
def getMaterial(id: str):
    if id not in env.repo:
        abort(404)
    item = env.repo[id]

    return jsonify(item)


@materials.route("/<id>/", methods=["DELETE"])
def deleteMaterial(id: str):
    if id not in env.repo:
        abort(404)
    del env.repo[id]
    return id


@materials.route("/", methods=["POST"])
def updateMaterial():
    obj = buildDocument(Material, request.get_json())

    env.repo.update(obj)
    return obj.id


@materials.route("/<id>/assets/<path:path>", methods=["GET"])
def assets(id: str, path: str):
    if id not in env.repo:
        abort(404)
    item = env.repo[id]
    return send_from_directory(item.assets, path)
