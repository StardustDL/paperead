import logging
import time
from typing import Optional

import click

from . import __version__


@click.command()
def run(schema: str, preview: bool = False) -> None:
    pass


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-v', '--verbose', count=True, default=0, type=click.IntRange(0, 4))
@click.option("--version", is_flag=True, default=False, help="Show the version.")
def main(ctx=None, verbose: int = 0, version: bool = False) -> None:
    """Paperead (https://github.com/StardustDL/paperead)"""
    click.echo(f"Welcome to Paperead v{__version__}!")

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
