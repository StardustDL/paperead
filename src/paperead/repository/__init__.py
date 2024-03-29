from datetime import datetime
import os
from pathlib import Path
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from typing import Any, Generic, Iterator, TypeVar

import yaml
from dateutil.tz import tzlocal

from paperead.repository.schema import resolveSchema

from .. import fsutils


@dataclass
class DocumentMetadata:
    name: str
    creation: datetime = field(
        default_factory=lambda: datetime.now(tzlocal()))
    modification: datetime = field(
        default_factory=lambda: datetime.now(tzlocal()))
    targets: dict[str, str] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    extra: dict[str, str] = field(default_factory=dict)
    schema: str = ""

    def toText(self) -> str:
        return yaml.safe_dump(asdict(self), sort_keys=False).strip()

    @classmethod
    def fromText(cls, text: str):
        data = yaml.safe_load(text)
        return cls(**data)


@dataclass
class Document(ABC):
    metadata: DocumentMetadata
    id: str = ""
    content: str = ""

    @classmethod
    def __metadata__(cls, name: str = "", text: str | None = None) -> DocumentMetadata:
        if text:
            return DocumentMetadata.fromText(text)
        else:
            return DocumentMetadata(name)

    def toText(self) -> str:
        return "\n".join(["---", self.metadata.toText(), "---", self.content])

    @classmethod
    def fromText(cls, id: str, text: str):
        lines = text.splitlines()
        try:
            frontIndex = lines.index("---")
            if frontIndex != 0:
                raise ValueError
            frontIndex = lines.index("---", 1)

            front = "\n".join(lines[1:frontIndex])
            content = "\n".join(lines[frontIndex+1:])
            metadata = cls.__metadata__(text=front)
        except ValueError:
            content = text
            metadata = cls.__metadata__(name=id)
        return cls(id=id, metadata=metadata, content=content)


TD = TypeVar("TD", bound=Document)


class DocumentRepository(ABC, Generic[TD]):
    def __init__(self, root: Path) -> None:
        self.root = root

    @classmethod
    @abstractmethod
    def __document__(cls, id: str, text: str | None = None) -> TD:
        pass

    def __documentPath__(self, id: str) -> Path:
        return self.root.joinpath(f"{id.strip()}.md")

    def __documentGlob__(self) -> str:
        return "*.md"

    def __postget__(self, path: Path, item: TD) -> None:
        pass

    def __postset__(self, path: Path, item: TD) -> None:
        pass

    def __postdel__(self, id: str, path: Path) -> None:
        pass

    def __oniter__(self, path: Path) -> str:
        return path.stem

    def __contains__(self, item: str) -> bool:
        path = self.__documentPath__(item)
        return path.exists() and path.is_file()

    def __getitem__(self, key: str) -> TD:
        if key in self:
            path = self.__documentPath__(key)
            result = self.__document__(
                key, path.read_text(encoding="utf-8"))
            resolved = resolveSchema(result.metadata.schema, result.content, path)
            result.metadata.schema = resolved.schema
            result.content = resolved.content
            self.__postget__(path, result)
            return result
        else:
            raise KeyError(key)

    def __setitem__(self, key: str, value: TD | None) -> None:
        if value:
            value.id = key
            self.update(value)
        else:
            self.create(key)

    def __delitem__(self, key: str) -> None:
        if key in self:
            path = self.__documentPath__(key)
            os.remove(path)
            self.__postdel__(key, path)

    def __iter__(self) -> Iterator[str]:
        for item in self.root.glob(self.__documentGlob__()):
            yield self.__oniter__(item)

    def __len__(self) -> int:
        return sum((1 for _ in self.root.glob(self.__documentGlob__())))

    def create(self, id: str) -> None:
        if id in self:
            raise Exception(f"Document with id '{id}' exists.")
        result = self.__document__(id)
        self.update(result)

    def update(self, item: TD) -> None:
        path = self.__documentPath__(item.id)
        text = item.toText()
        fsutils.ensureFile(path, text)
        self.__postset__(path, item)
