"""Parser file."""
import argparse

from .commands import select_command


def parse_cmd_input():
    """Create a parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, choices=[
        'highlight',
        'cowsay',
        'time',
        'help',
        ],
        help="""Available commands:
        highlight,
        cowsay,
        time,
        help,""")
    parser.add_argument('parametr', type=str, help=
        """Argument for highlight command is text\n
        Argument for cowsay command is text'\n
        Argument for time command region/city""")
    pars_args = parser.parse_args()
    select_command(pars_args.command, pars_args.parametr)
