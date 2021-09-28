import datetime
import itertools
import os
import pathlib
from dataclasses import asdict, dataclass, field
from typing import Dict, Iterator, Optional

import yaml
from dateutil.tz import tzlocal

from . import Description, DescriptionMetadata, DescriptionRepository


@dataclass
class NoteMetadata(DescriptionMetadata):
    extra: Dict[str, str] = field(default_factory=dict)


@dataclass
class Note(Description[NoteMetadata]):
    @classmethod
    def __metadata__(cls, name: str = "", text: Optional[str] = None) -> NoteMetadata:
        if text:
            return NoteMetadata.fromText(text)
        else:
            return NoteMetadata(name)


class NoteRepository(DescriptionRepository[Note]):
    def __init__(self, root: pathlib.Path) -> None:
        super().__init__(root)

    @classmethod
    def __description__(cls, id: str, text: Optional[str] = None) -> Note:
        if text:
            return Note.fromText(id, text)
        else:
            return Note(NoteMetadata(id), id)


if __name__ == "__main__":
    text = NoteMetadata("name").toText()
    print(text)
    print(NoteMetadata.fromText(text))

    manager = NoteRepository(pathlib.Path(
        __file__).parent.parent.parent.parent.parent.joinpath("temp").joinpath("notes"))

    del manager["a"]

    a = manager.create("a")
    a.content = "# abc\n"
    manager.update(a)

    print(a)
    import time

    time.sleep(1)

    print(manager["a"])

    print(list(manager))
