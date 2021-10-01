import pathlib
from . import app
from . import api
from .api import materials
from .api import notes
from . import frontend
from .frontend import wwwroot

import click
import os
import shutil
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi


def serve(debug: bool = False):
    from ..env import env

    if debug:
        app.run(host="0.0.0.0", port=env.serverConfig.port, debug=debug)
    else:
        click.echo(f"Listening on port {env.serverConfig.port}...")
        click.echo(f"Visit http://localhost:{env.serverConfig.port} to Paperead.")

        container = tornado.wsgi.WSGIContainer(app)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(env.serverConfig.port)
        tornado.ioloop.IOLoop.current().start()


def build(pyscript: bool = False):
    from ..env import env

    repo = env.repo

    dist = pathlib.Path(env.serverConfig.dist)
    if not dist.is_absolute():
        dist = pathlib.Path(env.path).joinpath(dist)

    if dist.exists() and dist.is_dir():
        click.echo(f"Delete existed dist at {dist.absolute()}.")
        shutil.rmtree(dist)

    shutil.copytree(wwwroot, dist)

    click.echo("Generating data.")

    apidist = dist.joinpath("api")
    os.mkdir(apidist)

    mdist = apidist.joinpath("materials")
    os.mkdir(mdist)

    with app.test_client() as c:
        mdist.joinpath("index.json").write_bytes(
            c.get(f"/api/materials/").data)

        for mid in repo:
            click.echo(f"Generating material {mid}.")

            mdir = mdist.joinpath(mid)
            os.mkdir(mdir)

            mdir.joinpath("index.json").write_bytes(
                c.get(f"/api/materials/{mid}/").data)

            click.echo(f"  Generating assets for material {mid}.")

            assets = repo.root.joinpath(mid).joinpath("assets")
            if assets.exists():
                shutil.copytree(
                    assets,
                    mdir.joinpath("assets"))

            click.echo(f"  Generating notes of material {mid}.")

            ndist = mdir.joinpath("notes")
            os.mkdir(ndist)
            ndist.joinpath("index.json").write_bytes(
                c.get(f"/api/materials/{mid}/notes/").data)

            nrepo = repo[mid].notes

            for nid in nrepo:
                click.echo(f"    Generating note {nid} of material {mid}.")

                ndir = ndist.joinpath(nid)
                os.mkdir(ndir)

                ndir.joinpath("index.json").write_bytes(
                    c.get(f"/api/materials/{mid}/notes/{nid}/").data)

    if pyscript:
        click.echo("Generating simple server python script.")
        click.echo(f"Use 'python serve.py' in {dist} to serve.")

        shutil.copy(pathlib.Path(__file__).parent.joinpath(
            "static.py"), dist.joinpath("serve.py"))
