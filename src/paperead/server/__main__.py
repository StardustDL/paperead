from pathlib import Path

from paperead.repository.materials import MaterialRepository

if __name__ == "__main__":
    from . import entrypoint
    from ..env import env
    env.setPath(Path(__file__).parent.parent.parent.parent.parent.joinpath(
        "temp").joinpath("materials"))
    entrypoint.serve(debug=True)
