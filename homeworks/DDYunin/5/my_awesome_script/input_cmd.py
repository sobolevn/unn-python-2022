import argparse

from my_awesome_script.commands import selected_command


def parse_cmd_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, choices=[
        'highlight',
        'cowsay',
        'time',
        'help',
        ],
        help='''1) Command: highlight\n
        2) Command: cowsay\n
        3) Command: time\n''',
        )
    parser.add_argument('parametr', type=str, help='''1) Argument: 'any text'\n
                        2) Argument: 'any text'\n
                        3) Argument: 'Region/City
                        (example: Europe/Moscow)\n''',
                        )
    pars_args = parser.parse_args()
    selected_command(pars_args.command, pars_args.parametr)
