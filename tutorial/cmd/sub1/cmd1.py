import subprocess
from cliff import command, lister


class TutorialSub1Command1(command.Command):
    _description = "Tutorial Subcommand1 Command1"

    def get_parser(self, prog_name):
        parser = super(TutorialSub1Command1, self).get_parser(prog_name)

        parser.add_argument('--arg1', required=True, type=str)

        return parser

    def take_action(self, parsed_args):
        ret = subprocess.check_call(["ls", "-l"])
        return {'hello': 'cliff'}


class TutorialSub1Command2(lister.Lister):
    _description = "Tutorial Subcommand1 Command2"

