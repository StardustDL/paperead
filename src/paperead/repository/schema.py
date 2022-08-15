from dataclasses import dataclass
from pathlib import Path
import sys
import subprocess
import marko
import logging
import os


@dataclass
class ResolvedSchema:
    schema: str
    content: str


def resolveDynamic(content: str, inputFile: Path) -> str | None:
    doc = marko.parse(content)
    for item in doc.children:
        if not isinstance(item, marko.parser.block.FencedCode):
            continue
        if item.lang != "python:exec":
            continue
        src = "\n".join((x.children for x in item.children))
        try:
            from ..env import env
            return subprocess.check_output([sys.executable, "-c", src], timeout=env.serverConfig.dynamicTimeout, cwd=inputFile.parent.absolute(), text=True, env=dict(os.environ, PAPEREAD_FILE=str(inputFile.absolute())))
        except Exception as ex:
            logging.error("Failed to resolve dynamic content", exc_info=ex)
            return None


def resolveSchema(schema: str, content: str, inputFile: Path) -> ResolvedSchema:
    if schema.startswith("dynamic:"):
        newContent = resolveDynamic(content, inputFile)
        content = newContent if newContent is not None else ""
        schema = schema.split(":")[-1]
    return ResolvedSchema(schema, content)
