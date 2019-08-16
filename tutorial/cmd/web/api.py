import io
import json
import logging

from flask import Flask
from cliff import command

from flask_restplus import Resource, Api, fields, reqparse

from tutorial.shell import Tutorial
from tutorial.cmd.sub1.cmd1 import TutorialSub1Command1
from tutorial.cmd.sub1.cmd1 import TutorialSub1Command2
from tutorial.cmd.sub2.cmd1 import TutorialSub2Command1

API = Api()


class StringStream(io.StringIO):
    def __init__(self):
        super().__init__()
        self.str = ''

    def write(self, chunk):
        self.str += chunk

    def read(self, *args, **kwargs):
        return self.str


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


ns = API.namespace('sub1')


@ns.route('/api/v1/sub1/cmd1', methods=['GET', 'POST', 'DELETE'])
class Sub1Cmd1(Resource):
    @ns.doc('get')
    @ns.param('arg1', 'String value')
    @ns.param('arg2', 'String value')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arg1', required=True, type=str, location='args')
        parser.add_argument('arg2', required=True, type=str, location='args')
        args = parser.parse_args()

        ss = StringStream()
        ret = TutorialSub1Command1(Tutorial(stdout=ss), args, 'sub1 cmd1').run(args)
        return ret


@ns.route('/api/v1/sub1/cmd2', methods=['GET', 'POST', 'DELETE'])
class Sub1Cmd1(Resource):
    @ns.doc('get')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('formatter', default='json')
        parser.add_argument('sort_columns')
        parser.add_argument('columns')
        parser.add_argument('noindent')
        args = parser.parse_args()

        ss = StringStream()
        TutorialSub1Command2(Tutorial(stdout=ss), args, 'sub2 cmd1').run(args)
        return json.load(ss)
