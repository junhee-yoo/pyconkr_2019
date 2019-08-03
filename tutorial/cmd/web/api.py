import logging

from flask import Flask
from cliff import command

from flask_restplus import Resource, Api, fields, reqparse

from tutorial.shell import Tutorial
from tutorial.cmd.sub1.cmd1 import TutorialSub1Command1
from tutorial.cmd.sub2.cmd1 import TutorialSub2Command1

API = Api()


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


@API.route('/api/v1/sub1/cmd1', methods=['GET', 'POST', 'DELETE'])
class Sub1Cmd1(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arg1', required=True, type=str, location='args')
        args = parser.parse_args()

        ret = TutorialSub1Command1(Tutorial.instance(), args, 'sub1 cmd1').run(args)
        return ret


@API.route('/api/v1/sub2/cmd1', methods=['GET', 'POST', 'DELETE'])
class Sub1Cmd1(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()

        ret = TutorialSub2Command1(Tutorial.instance(), args, 'sub2 cmd1').run(args)
        return ret
