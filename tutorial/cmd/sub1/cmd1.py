import argparse
import subprocess
from cliff import command, lister


def type_check(arg):
    if 'i' in arg:
        return arg

    raise argparse.ArgumentTypeError("'i' is not in arg")


class TutorialSub1Command1(command.Command):
    _description = "Tutorial Subcommand1 Command1"

    def get_parser(self, prog_name):
        parser = super(TutorialSub1Command1, self).get_parser(prog_name)

        parser.add_argument('--arg1', required=True, type=str)
        parser.add_argument('--arg2', required=True, type=type_check)

        return parser

    def take_action(self, parsed_args):
        ret = subprocess.check_call(["ls", "-l"])
        return {'hello': 'cliff',
                'args': parsed_args}


class TutorialSub1Command2(lister.Lister):
    _description = "Tutorial Subcommand1 Command2"

    def take_action(self, parsed_args):
        return ('col1', 'col2'), [('data1', 'data1'), ('data2', 'data2')]
