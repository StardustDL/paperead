import pathlib
from typing import Optional
from ..repository.materials import MaterialRepository

class Environment:
    def __init__(self, repo: MaterialRepository) -> None:
        self.repo = repo

env: Environment = Environment(MaterialRepository(pathlib.Path(".")))