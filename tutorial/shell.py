import os
import sys
import configparser

from cliff.app import App

from tutorial.common.commandmanager import CommandManager

APP = None


class Tutorial(App):
    """
    Cliff Tutorial
    """
    def __init__(self):
        super(Tutorial, self).__init__(
            description='cliff tutorial',
            version='0.0.1',
            command_manager=CommandManager('tutorial.cli'),
            deferred_help=True,
        )
        self.config = None

    @staticmethod
    def get_instance():
        global APP
        if not APP:
            APP = Tutorial()

        return APP

    def build_option_parser(self, description, version,
                            argparse_kwargs=None):
        parser = super(Tutorial, self).build_option_parser(description, version,
                                                           argparse_kwargs=argparse_kwargs)  # noqa
        parser.add_argument(
            '--config',
            metavar='<config-file-path>',
            default=f'{os.getenv("HOME")}/.tutorial/config'
        )

        return parser

    def initialize_app(self, argv):
        self.LOG.debug('initializing_app')
        # TODO(jhyoo): change this to plug-in structure
        self.command_manager.add_command_group('tutorial.cli.sub1')
        self.command_manager.add_command_group('tutorial.cli.sub2')
        config_path = self.options.config
        if os.path.exists(config_path):
            self.config = configparser.ConfigParser()
            self.config.read(config_path)

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    ret = Tutorial.get_instance().run(argv)
    if isinstance(ret, dict):
        print(ret)
        return 0

    return ret


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
