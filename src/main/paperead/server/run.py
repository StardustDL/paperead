import pathlib

import click
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi

from paperead.repository.materials import MaterialRepository


def run(repo: MaterialRepository, port: int = 3649, debug: bool = False):
    from . import app
    from . import api, env
    from .api import materials
    from .api import notes
    from . import frontend

    env.baseUrl = f"http://localhost:{port}"
    env.repo = repo

    if debug:
        app.run(host="0.0.0.0", port=port, debug=debug)
    else:
        click.echo(f"Listening on port {port}...")
        click.echo(f"Visit {env.baseUrl} to Paperead.")

        container = tornado.wsgi.WSGIContainer(app)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(port)
        tornado.ioloop.IOLoop.current().start()
