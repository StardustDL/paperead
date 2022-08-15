import logging
import os
import pathlib
import click

__version__ = "0.2.6"


def get_app_directory():
    return pathlib.Path(__file__).parent
