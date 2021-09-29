import pathlib

import click
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi

from paperead.repository.materials import MaterialRepository


def run(debug: bool = False):
    from ..env import env
    from . import app
    from . import api
    from .api import materials
    from .api import notes
    from . import frontend

    if debug:
        app.run(host="0.0.0.0", port=env.serverConfig.port, debug=debug)
    else:
        click.echo(f"Listening on port {env.serverConfig.port}...")
        click.echo(f"Visit http://localhost:{env.baseUrl} to Paperead.")

        container = tornado.wsgi.WSGIContainer(app)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(env.serverConfig.port)
        tornado.ioloop.IOLoop.current().start()
