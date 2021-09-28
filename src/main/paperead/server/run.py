import pathlib

from paperead.repository.materials import MaterialRepository


def runInDirectory(path: pathlib.Path, port: int = 3649):
    from . import app
    from . import api, env
    from .api import materials
    from .api import notes
    from . import frontend

    env.baseUrl = f"http://localhost:{port}"
    env.repo = MaterialRepository(path)

    app.run(host="0.0.0.0", port=port, debug=True)
