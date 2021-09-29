import datetime
import itertools
import os
import pathlib
from dataclasses import asdict, dataclass, field
from typing import Dict, Iterator, Optional

import yaml
from dateutil.tz import tzlocal

from . import Description, DescriptionRepository
from .base import BaseMetadata


@dataclass
class NoteMetadata(BaseMetadata):
    pass


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
