import pathlib
from paperead.repository.materials import MaterialRepository


if __name__ == "__main__":
    from . import api, env
    from .api import materials
    from .api import notes

    env.repo = MaterialRepository(pathlib.Path(__file__).parent.parent.parent.parent.parent.joinpath("temp").joinpath("materials"))

    api.app.run(host="0.0.0.0", port=3649, debug=True)