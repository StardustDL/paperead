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


@dataclass
class BaseMetadata(DescriptionMetadata):
    targets: Dict[str, str] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    extra: Dict[str, str] = field(default_factory=dict)
