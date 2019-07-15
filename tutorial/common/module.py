from cliff.lister import Lister


class ListCommand(Lister):
    def get_parser(self, prog_name):
        parser = super(ListCommand, self).get_parser(prog_name)
        parser.add_argument(
            '--group',
            metavar='<group-keyword>',
            help='Show commands'
        )
        return parser

    def take_action(self, parsed_args):
        cm = self.app.command_manager
        groups = cm.get_command_groups()
        groups = sorted(groups)
        columns = ('Command Group', 'Commands')

        if parsed_args.group:
            groups = (group for group in groups if parsed_args.group in group)

        commands = []
        for group in groups:
            command_names = cm.get_command_names(group)
            command_names = sorted(command_names)

            if command_names:
                commands.append((group, command_names))

        return columns, commands
