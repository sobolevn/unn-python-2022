"""Poetry shell parser."""
from argparse import ArgumentParser

from my_awesome_script.commands import run_command


def create_parser():
    """
    Create a poetry shell parser.

    :return:
    """
    parser = ArgumentParser()
    parser.add_argument('command', type=str, help='imput command')
    parser.add_argument('text', type=str)
    args = parser.parse_args()

    command = args.command
    text = args.text

    run_command(command)(text)
