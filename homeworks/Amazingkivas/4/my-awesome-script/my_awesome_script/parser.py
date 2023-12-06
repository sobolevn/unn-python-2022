"""Poetry shell parser."""
from argparse import ArgumentParser

from my_awesome_script.commands import run_command


def create_parser():
    """
    Create a poetry shell parser.

    :return:
    """
    parser = ArgumentParser()
    parser.add_argument('command', type=str, help=', '.join(commands))
    parser.add_argument('parameter', type=str, help=', '.join(comm_param))
    args = parser.parse_args()

    command = args.command
    parameter = args.parameter

    run_command(command)(parameter)


commands = ('highlight', 'cowsay', 'time')
comm_param = ('code to highlight', 'text that the cow say', 'selected region')
