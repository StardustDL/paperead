import datetime
import itertools
import os
import pathlib
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from typing import Any, Generic, Iterator, Optional, TypeVar

import yaml
from dateutil.tz import tzlocal

from .. import fsutils


@dataclass
class DescriptionMetadata(ABC):
    name: str
    creation: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(tzlocal()))
    modification: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(tzlocal()))

    def toText(self) -> str:
        return yaml.safe_dump(asdict(self), sort_keys=False).strip()

    @classmethod
    def fromText(cls, text: str):
        data = yaml.safe_load(text)
        return cls(**data)


TM = TypeVar("TM", bound=DescriptionMetadata)


@dataclass
class Description(ABC, Generic[TM]):
    metadata: TM
    id: str = ""
    content: str = ""

    @classmethod
    @abstractmethod
    def __metadata__(cls, name: str = "", text: Optional[str] = None) -> TM:
        pass

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


TD = TypeVar("TD", bound=Description)


class DescriptionRepository(ABC, Generic[TD]):
    def __init__(self, root: pathlib.Path) -> None:
        self.root = root

    @classmethod
    @abstractmethod
    def __description__(cls, id: str, text: Optional[str] = None) -> TD:
        pass

    def __descriptionPath__(self, id: str) -> pathlib.Path:
        return self.root.joinpath(f"{id.strip()}.md")

    def __descriptionGlob__(self) -> str:
        return "*.md"

    def __postget__(self, path: pathlib.Path, item: TD) -> None:
        pass

    def __postset__(self, path: pathlib.Path, item: TD) -> None:
        pass

    def __postdel__(self, id: str, path: pathlib.Path) -> None:
        pass

    def __oniter__(self, path: pathlib.Path) -> str:
        return path.stem

    def __contains__(self, item: str) -> bool:
        path = self.__descriptionPath__(item)
        return path.exists() and path.is_file()

    def __getitem__(self, key: str) -> TD:
        if key in self:
            path = self.__descriptionPath__(key)
            result = self.__description__(
                key, path.read_text(encoding="utf-8"))
            self.__postget__(path, result)
            return result
        else:
            raise KeyError(key)

    def __setitem__(self, key: str, value: Optional[TD]) -> None:
        if value:
            value.id = key
            self.update(value)
        else:
            self.create(key)

    def __delitem__(self, key: str) -> None:
        if key in self:
            path = self.__descriptionPath__(key)
            os.remove(path)
            self.__postdel__(key, path)

    def __iter__(self) -> Iterator[str]:
        for item in self.root.glob(self.__descriptionGlob__()):
            yield self.__oniter__(item)

    def __len__(self) -> int:
        return sum((1 for _ in self.root.glob(self.__descriptionGlob__())))

    def create(self, id: str) -> None:
        if id in self:
            raise Exception(f"Description with id '{id}' exists.")
        result = self.__description__(id)
        self.update(result)

    def update(self, item: TD) -> None:
        path = self.__descriptionPath__(item.id)
        text = item.toText()
        fsutils.ensureFile(path, text)
        self.__postset__(path, item)
