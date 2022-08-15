import datetime
import itertools
import os
from pathlib import Path
import shutil
from dataclasses import asdict, dataclass, field

import yaml
from dateutil.tz import tzlocal

from .. import fsutils
from . import Document, DocumentMetadata, DocumentRepository
from .notes import NoteRepository


@dataclass
class Material(Document):
    @property
    def notes(self) -> NoteRepository | None:
        if hasattr(self, '_notes'):
            return self._notes
        else:
            return None

    @notes.setter
    def notes(self, value: NoteRepository):
        self._notes = value

    @property
    def assets(self) -> Path | None:
        if hasattr(self, '_assets'):
            return self._assets
        else:
            return None

    @assets.setter
    def assets(self, value: Path):
        self._assets = value


class MaterialRepository(DocumentRepository[Material]):
    def __init__(self, root: Path) -> None:
        super().__init__(root)

    @classmethod
    def __document__(cls, id: str, text: str | None = None) -> Material:
        if text:
            return Material.fromText(id, text)
        else:
            return Material(DocumentMetadata(id), id)

    def __documentPath__(self, id: str) -> Path:
        return self.root.joinpath(id.strip()).joinpath("description.md")

    def __documentGlob__(self) -> str:
        return "*/description.md"

    def __oniter__(self, path: Path) -> str:
        return path.parent.stem

    def _getNotesPath(self, path: Path) -> Path:
        return path.parent.joinpath("notes")

    def _getAssetsPath(self, path: Path) -> Path:
        return path.parent.joinpath("assets")

    def __postget__(self, path: Path, item: Material) -> None:
        item.notes = NoteRepository(self._getNotesPath(path))
        item.assets = self._getAssetsPath(path)

    def __postset__(self, path: Path, item: Material) -> None:
        subroot = path.parent
        fsutils.ensureDirectory(subroot.joinpath("assets"))
        fsutils.ensureDirectory(subroot.joinpath("notes"))

    def __postdel__(self, id: str, path: Path) -> None:
        shutil.rmtree(path.parent)
