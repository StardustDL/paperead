import mimetypes
import pathlib
from typing import Optional

from flask import Flask

from flask_cors import CORS

from ..repository.materials import MaterialRepository


class Environment:
    def __init__(self, repo: MaterialRepository) -> None:
        self.repo = repo
        self.baseUrl = ""


env: Environment = Environment(MaterialRepository(pathlib.Path(".")))


mimetypes.add_type("text/css", ".css")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("text/javascript", ".mjs")

app = Flask(__name__)
CORS(app)
