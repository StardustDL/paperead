from dataclasses import dataclass
import pathlib
import sys
import subprocess
from typing import Optional
import marko
import logging


@dataclass
class ResolvedSchema:
    schema: str
    content: str


def resolveDynamic(content: str, workingDir: pathlib.Path) -> Optional[str]:
    doc = marko.parse(content)
    for item in doc.children:
        if not isinstance(item, marko.parser.block.FencedCode):
            continue
        if item.lang != "python:exec":
            continue
        src = "\n".join((x.children for x in item.children))
        try:
            return subprocess.check_output([sys.executable, "-c", src], timeout=60, cwd=workingDir.absolute(), text=True)
        except Exception as ex:
            logging.error("Failed to resolve dynamic content", exc_info=ex)
            return None


def resolveSchema(schema: str, content: str, workingDir: pathlib.Path) -> ResolvedSchema:
    if schema.startswith("dynamic:"):
        newContent = resolveDynamic(content, workingDir)
        content = newContent if newContent is not None else ""
        schema = schema.split(":")[-1]
    return ResolvedSchema(schema, content)
