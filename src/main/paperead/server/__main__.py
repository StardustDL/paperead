import pathlib

from paperead.repository.materials import MaterialRepository

if __name__ == "__main__":
    from . import run
    from ..env import env
    env.setPath(pathlib.Path(__file__).parent.parent.parent.parent.parent.joinpath(
        "temp").joinpath("materials"))
    run.run(debug=True)
