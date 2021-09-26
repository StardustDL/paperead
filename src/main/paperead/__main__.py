import logging
import time
import pathlib
from typing import Optional

import click

from . import __version__


@click.command()
def run() -> None:
    pass


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-D', '--directory', type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=pathlib.Path), default=".", help="Path to working directory.")
@click.option('-v', '--verbose', count=True, default=0, type=click.IntRange(0, 4))
@click.option("--version", is_flag=True, default=False, help="Show the version.")
def main(ctx=None, directory: pathlib.Path = ".", verbose: int = 0, version: bool = False) -> None:
    """Paperead (https://github.com/StardustDL/paperead)"""
    click.echo(f"Welcome to Paperead v{__version__}!")
    click.echo(f"Working directory: {click.format_filename(directory)}")

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

    if version:
        click.echo(f"Paperead v{__version__}")
        exit(0)


main.add_command(run)

if __name__ == '__main__':
    main()
