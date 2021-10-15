import logging
import pathlib
import time
from typing import Optional

import click
from click import BadArgumentUsage, BadOptionUsage, BadParameter
from click.exceptions import ClickException

from . import __version__
from .repository.materials import MaterialRepository

from .env import env, DEFAULT_BUILD_HOST, DEFAULT_BUILD_DIST, DEFAULT_SERVER_PORT


def setWorkingDirectory(wdir: pathlib.Path):
    env.setPath(wdir)


@click.command()
@click.option("-p", "--port", default=None, help="Port to serve.")
@click.option("-d", "--debug", is_flag=True, default=False, help="Debug mode.")
def serve(port: Optional[int] = None, debug: bool = False) -> None:
    """Serve websites."""
    from .server import entrypoint
    if port:
        env.serverConfig.port = port
    entrypoint.serve(debug)


@click.command()
@click.option("-h", "--host", default=None, type=click.Choice(["empty", "python", "netlify"]), help="Host for the static website.")
@click.option("-d", "--dist", default=None, help="Directory for building output.")
def build(host: Optional[str] = None, dist: Optional[str] = None) -> None:
    """Build static website."""
    from .server import entrypoint
    if host:
        env.buildConfig.host = host
    if dist:
        env.buildConfig.dist = dist
    entrypoint.build()


@click.command()
def init() -> None:
    """Initialize config files of paperead."""
    env.generateConfigFile()


@click.command()
@click.argument("id")
@click.option("-N", "--note", default="", help="Create a new note with specified id.")
def new(id: str, note: str = "") -> None:
    """Create a new material or note."""
    if note:
        if id not in env.repo:
            raise ClickException(f"Not found material with id '{id}'.")

        material = env.repo[id]
        if note in material.notes:
            raise ClickException(
                f"Note with id '{note}' exists for material with id '{id}'.")

        material.notes.create(note)

        click.echo(
            f"Created note with id '{note}' for material with id '{id}'.")
    else:
        if id in env.repo:
            raise ClickException(f"Material with id '{id}' exists.")

        env.repo.create(id)

        click.echo(f"Created material with id '{id}'.")


@click.command()
@click.argument("id")
@click.option("-N", "--note", default="", help="Remove a note with specified id.")
def rm(id: str, note: str = "") -> None:
    """Remove a material or note."""

    if note:
        if id not in env.repo:
            raise ClickException(f"Not found material with id '{id}'.")

        material = env.repo[id]
        if note not in material.notes:
            raise ClickException(
                f"Not found note with id '{note}' for material with id '{id}'.")

        del material.notes[note]

        click.echo(
            f"Removed note with id '{note}' for material with id '{id}'.")
    else:
        if id not in env.repo:
            raise ClickException(f"Not found material with id '{id}'.")

        del env.repo[id]

        click.echo(f"Removed material with id '{id}'.")


@click.command()
@click.argument("id", default="")
def list(id: str = "") -> None:
    """List materials and notes."""

    if id:
        if id not in env.repo:
            raise ClickException(f"Not found material with id '{id}'.")

        material = env.repo[id]

        for item in material.notes:
            click.echo(item)
    else:
        for item in env.repo:
            click.echo(item)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-D', '--directory', type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=pathlib.Path), default=".", help="Path to working directory.")
@click.option('-v', '--verbose', count=True, default=0, type=click.IntRange(0, 4))
@click.option("--version", is_flag=True, default=False, help="Show the version.")
def main(ctx=None, directory: pathlib.Path = ".", verbose: int = 0, version: bool = False) -> None:
    """Paperead (https://github.com/StardustDL/paperead)"""

    # click.echo(f"Welcome to Paperead v{__version__}!")

    setWorkingDirectory(directory)

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

    logger.info(f"Working directory: {click.format_filename(env.path)}")

    if version:
        click.echo(f"Paperead v{__version__}")
        exit(0)


main.add_command(serve)
main.add_command(build)
main.add_command(init)
main.add_command(new)
main.add_command(rm)
main.add_command(list)

if __name__ == '__main__':
    main()
