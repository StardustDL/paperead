import logging
import pathlib
import time
from typing import Optional

import click
from click import BadArgumentUsage, BadOptionUsage, BadParameter
from click.exceptions import ClickException

from . import __version__
from .repository.materials import MaterialRepository

workingDir = pathlib.Path(".")


@click.command()
def serve() -> None:
    """Serve websites."""
    from .server import run
    run.runInDirectory(workingDir)


@click.command()
@click.argument("id")
def new(id: str) -> None:
    repo = MaterialRepository(workingDir)
    repo.create(id)


@click.command()
@click.argument("id")
@click.option("-N", "--note", default="", help="Create a new note with specified id.")
def new(id: str, note: str = "") -> None:
    """Create a new material or note."""
    repo = MaterialRepository(workingDir)

    if note:
        if id not in repo:
            raise ClickException(f"Not found material with id '{id}'.")

        material = repo[id]
        if note in material.notes:
            raise ClickException(
                f"Note with id '{note}' exists for material with id '{id}'.")

        material.notes.create(note)

        click.echo(
            f"Created note with id '{note}' for material with id '{id}'.")
    else:
        if id in repo:
            raise ClickException(f"Material with id '{id}' exists.")

        repo.create(id)

        click.echo(f"Created material with id '{id}'.")


@click.command()
@click.argument("id")
@click.option("-N", "--note", default="", help="Remove a note with specified id.")
def rm(id: str, note: str = "") -> None:
    """Remove a material or note."""
    repo = MaterialRepository(workingDir)

    if note:
        if id not in repo:
            raise ClickException(f"Not found material with id '{id}'.")

        material = repo[id]
        if note not in material.notes:
            raise ClickException(
                f"Not found note with id '{note}' for material with id '{id}'.")

        del material.notes[note]

        click.echo(
            f"Removed note with id '{note}' for material with id '{id}'.")
    else:
        if id not in repo:
            raise ClickException(f"Not found material with id '{id}'.")

        del repo[id]

        click.echo(f"Removed material with id '{id}'.")


@click.command()
@click.argument("id", default="")
# @click.option("-N", "--note", default="", help="List notes for material with specified id.")
def list(id: str = "") -> None:
    """List materials and notes."""
    repo = MaterialRepository(workingDir)

    if id:
        if id not in repo:
            raise ClickException(f"Not found material with id '{id}'.")

        material = repo[id]

        for item in material.notes:
            click.echo(item)
    else:
        for item in repo:
            click.echo(item)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-D', '--directory', type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=pathlib.Path), default=".", help="Path to working directory.")
@click.option('-v', '--verbose', count=True, default=0, type=click.IntRange(0, 4))
@click.option("--version", is_flag=True, default=False, help="Show the version.")
def main(ctx=None, directory: pathlib.Path = ".", verbose: int = 0, version: bool = False) -> None:
    """Paperead (https://github.com/StardustDL/paperead)"""

    global workingDir

    # click.echo(f"Welcome to Paperead v{__version__}!")

    workingDir = directory

    logger = logging.getLogger("Cli-Main")

    loggingLevel = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
        4: logging.NOTSET
    }[verbose]

    logging.basicConfig(level=loggingLevel)

    logger.debug(f"Logging level: {loggingLevel}")

    logger.info(f"Working directory: {click.format_filename(workingDir)}")

    if version:
        click.echo(f"Paperead v{__version__}")
        exit(0)


main.add_command(serve)
main.add_command(new)
main.add_command(rm)
main.add_command(list)

if __name__ == '__main__':
    main()
