import pathlib
from paperead.repository.materials import MaterialRepository


def runInDirectory(path: pathlib.Path, port: int = 3649):
    from . import api, env
    from .api import materials
    from .api import notes

    env.baseUrl = f"http://localhost:{port}"
    env.repo = MaterialRepository(path)

    api.app.run(host="0.0.0.0", port=port, debug=True)