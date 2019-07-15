from flask_restplus import Resource, Api, fields, reqparse

from tutorial.shell import Tutorial
from tutorial.cmd.sub1.cmd1 import TutorialSub1Command1

API = Api()
CLI_APP = Tutorial.get_instance()


@API.route('/api/v1/sub1/cmd1', methods=['GET', 'POST', 'DELETE'])
class Sub1Cmd1(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arg1', required=True, type=str, location='args')
        args = parser.parse_args()

        ret = TutorialSub1Command1(None, None, None).run(args)
        return ret
