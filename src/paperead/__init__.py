import logging
import os
from pathlib import Path
import click

__version__ = "0.2.6"


def get_app_directory() -> Path:
    return Path(__file__).parent
