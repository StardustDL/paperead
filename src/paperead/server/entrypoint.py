import pathlib

import click
import os
import shutil
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
from flask import request, abort


def buildApp():
    from . import app
    from .api import build as apiBuild
    from .frontend import frontend

    app.register_blueprint(apiBuild(), url_prefix="/api")
    app.register_blueprint(frontend, url_prefix="/")

    return app


def serve(debug: bool = False):
    from ..env import env
    
    app = buildApp()

    if env.serverConfig.auth:
        app.config["BASIC_AUTH_USERNAME"] = "admin"
        app.config["BASIC_AUTH_PASSWORD"] = str(env.serverConfig.auth)
        app.config["BASIC_AUTH_FORCE"] = True

        from flask_basicauth import BasicAuth
        BasicAuth(app)

    if env.serverConfig.readonly:
        @app.before_request
        def readonly():
            if request.method not in {"GET", "HEAD", "OPTIONS"}:
                abort(403)

    if debug:
        app.run(host="0.0.0.0", port=env.serverConfig.port, debug=debug)

    else:
        click.echo(f"Listening on port {env.serverConfig.port}...")
        click.echo(
            f"Visit http://localhost:{env.serverConfig.port} to Paperead.")

        container = tornado.wsgi.WSGIContainer(app)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(env.serverConfig.port)
        tornado.ioloop.IOLoop.current().start()


def build():
    from ..env import env
    from .frontend import wwwroot

    repo = env.repo

    dist = pathlib.Path(env.buildConfig.dist)
    if not dist.is_absolute():
        dist = pathlib.Path(env.path).joinpath(dist)

    if dist.exists() and dist.is_dir():
        click.echo(f"Delete existed dist at {dist.absolute()}.")
        shutil.rmtree(dist)

    click.echo("Generating frontend.")

    shutil.copytree(wwwroot, dist)

    click.echo("Generating data.")

    app = buildApp()

    with app.test_client() as c:
        apidist = dist.joinpath("api")
        os.mkdir(apidist)

        apidist.joinpath("index.json").write_bytes(
            c.get(f"/api/").data)

        mdist = apidist.joinpath("materials")
        os.mkdir(mdist)

        mdist.joinpath("index.json").write_bytes(
            c.get(f"/api/materials/").data)

        for mid in repo:
            click.echo(f"  Generating material {mid}.")

            mdir = mdist.joinpath(mid)
            os.mkdir(mdir)

            mdir.joinpath("index.json").write_bytes(
                c.get(f"/api/materials/{mid}/").data)

            mdata = repo[mid]

            assets = mdata.assets
            if assets and assets.exists():
                click.echo(f"    Generating assets.")
                shutil.copytree(
                    assets,
                    mdir.joinpath("assets"))

            click.echo(f"    Generating notes.")

            ndist = mdir.joinpath("notes")
            os.mkdir(ndist)
            ndist.joinpath("index.json").write_bytes(
                c.get(f"/api/materials/{mid}/notes/").data)

            nrepo = mdata.notes

            for nid in nrepo:
                click.echo(f"      Generating note {nid}.")

                ndir = ndist.joinpath(nid)
                os.mkdir(ndir)

                ndir.joinpath("index.json").write_bytes(
                    c.get(f"/api/materials/{mid}/notes/{nid}/").data)

    staticPath = pathlib.Path(__file__).parent.joinpath("static")

    if env.buildConfig.host == 'python':
        click.echo("Generating files for python host.")
        click.echo(f"Use 'python serve.py' in {dist} to serve.")

        shutil.copyfile(staticPath.joinpath("__main__.py"),
                        dist.joinpath("serve.py"))
    elif env.buildConfig.host == 'netlify':
        click.echo("Generating files for netlify host.")
        shutil.copyfile(staticPath.joinpath("netlify").joinpath(
            "netlify.toml"), dist.joinpath("netlify.toml"))
