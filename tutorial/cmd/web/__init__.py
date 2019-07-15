import logging

from flask import Flask
from cliff import command

from tutorial.cmd.web.api import API


class RestAPIServe(command.Command):
    _log = logging.getLogger(__name__)
    _description = 'Tutorial RESTful server launch'

    def get_parser(self, prog_name):
        parser = super(RestAPIServe, self).get_parser(prog_name)
        parser.add_argument(
            '--port',
            metavar='<port>',
            help='port for HTTP serving.'
        )
        return parser

    def take_action(self, parsed_args):
        app = Flask('Tutorial')
        API.init_app(app)
        return app.run(debug=True, host='0.0.0.0', port=getattr(parsed_args, 'port', 8080))
