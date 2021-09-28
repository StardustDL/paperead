import datetime
import itertools
import os
import pathlib
import shutil
from dataclasses import asdict, dataclass, field
from typing import Dict, Iterator, List, Optional

import yaml
from dateutil.tz import tzlocal

from paperead import fsutils
from paperead.repository import (Description, DescriptionMetadata,
                                 DescriptionRepository)
from paperead.repository.notes import NoteRepository


@dataclass
class MaterialMetadata(DescriptionMetadata):
    targets: Dict[str, str] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    extra: Dict[str, str] = field(default_factory=dict)


@dataclass
class Material(Description[MaterialMetadata]):
    @classmethod
    def __metadata__(cls, name: str = "", text: Optional[str] = None) -> MaterialMetadata:
        if text:
            return MaterialMetadata.fromText(text)
        else:
            return MaterialMetadata(name)

    @property
    def notes(self) -> Optional[NoteRepository]:
        if hasattr(self, '_notes'):
            return self._notes
        else:
            return None

    @notes.setter
    def notes(self, value: NoteRepository):
        self._notes = value

    @property
    def assets(self) -> Optional[pathlib.Path]:
        if hasattr(self, '_assets'):
            return self._assets
        else:
            return None

    @assets.setter
    def assets(self, value: pathlib.Path):
        self._assets = value


class MaterialRepository(DescriptionRepository[Material]):
    def __init__(self, root: pathlib.Path) -> None:
        super().__init__(root)

    @classmethod
    def __description__(cls, id: str, text: Optional[str] = None) -> Material:
        if text:
            return Material.fromText(id, text)
        else:
            return Material(MaterialMetadata(id), id)

    def __descriptionPath__(self, id: str) -> pathlib.Path:
        return self.root.joinpath(id.strip()).joinpath("description.md")

    def __descriptionGlob__(self) -> str:
        return "*/description.md"

    def __oniter__(self, path: pathlib.Path) -> str:
        return path.parent.stem

    def _getNotesPath(self, path: pathlib.Path) -> pathlib.Path:
        return path.parent.joinpath("notes")

    def _getAssetsPath(self, path: pathlib.Path) -> pathlib.Path:
        return path.parent.joinpath("assets")

    def __postget__(self, path: pathlib.Path, item: Material) -> None:
        item.notes = NoteRepository(self._getNotesPath(path))
        item.assets = self._getAssetsPath(path)

    def __postset__(self, path: pathlib.Path, item: Material) -> None:
        subroot = path.parent
        fsutils.ensureDirectory(subroot.joinpath("assets"))
        fsutils.ensureDirectory(subroot.joinpath("notes"))

    def __postdel__(self, id: str, path: pathlib.Path) -> None:
        shutil.rmtree(path.parent)


if __name__ == "__main__":
    m = MaterialMetadata("name")
    m.tags.append("123")
    m.targets.append("www.example.com")
    text = m.toText()
    print(text)
    print(MaterialMetadata.fromText(text))

    m = Material(MaterialMetadata("a"), "a")
    print(m)

    manager = MaterialRepository(pathlib.Path(
        __file__).parent.parent.parent.parent.parent.joinpath("temp").joinpath("materials"))

    del manager["a"]

    a = manager.create("a")
    a.content = "# abc\n"
    manager.update(a)

    print(manager["a"])

    print(list(manager))
