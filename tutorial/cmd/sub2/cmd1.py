from cliff import command

class TutorialSub2Command1(command.Command):
    def get_parser(self, prog_name):
        return super(TutorialSub2Command1, self).get_parser(prog_name)

    def take_action(self, parsed_args):
        print("TutorialSub2Command1")
        return True
