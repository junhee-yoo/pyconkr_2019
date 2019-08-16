import argparse
import subprocess
from cliff import command, lister, hooks


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
        output = subprocess.check_output(["ps", "aux"]).decode('utf-8')

        def handle(row):
            s = row.split()
            return "{}: {}".format(s[0], s[1])

        ret = list(map(lambda row: handle(row), filter(lambda l: parsed_args.arg1 in l, output.split('\n'))))

        return {'hello': 'cliff',
                'args': parsed_args,
                'output': "\n".join(ret)}


class TutorialSub1Command1Hook(hooks.CommandHook):
    def get_parser(self, parser):
        # parser.add_argument('--hook')
        return parser

    def get_epilog(self):
        return 'this is from hook'

    def before(self, parsed_args):
        self.cmd.app.stdout.write('before\n')

    def after(self, parsed_args, return_code):
        return_code['from_hook'] = "I'm from hook!"
        return return_code


class TutorialSub1Command2(lister.Lister):
    _description = "Tutorial Subcommand1 Command2"

    def take_action(self, parsed_args):
        return ('col1', 'col2'), [('data1', 'data1'), ('data2', 'data2')]
