import datetime
import itertools
import os
from pathlib import Path
from dataclasses import asdict, dataclass, field
from typing import Dict, Iterator, Optional

import yaml
from dateutil.tz import tzlocal

from . import Document, DocumentMetadata, DocumentRepository


@dataclass
class Note(Document):
    pass


class NoteRepository(DocumentRepository[Note]):
    def __init__(self, root: Path) -> None:
        super().__init__(root)

    @classmethod
    def __document__(cls, id: str, text: str | None = None) -> Note:
        if text:
            return Note.fromText(id, text)
        else:
            return Note(DocumentMetadata(id), id)
