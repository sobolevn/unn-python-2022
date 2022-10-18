import argparse
from .commands import highligh, cowsay, time

comands_dict = {'highligh': highligh, 'cowsay': cowsay, 'time': time}


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', type=str,
                        choices=['highligh', 'cowsay', 'time'],
                        help='Enter comand from this list'
                        )
    parser.add_argument('param', type=str,
                        help='''Enter <text> for highligh or cowsay,
                        or <Region/City> for time'''
                        )
    args = parser.parse_args()
    use_comand(args.operation, args.param)


def use_comand(comand, param):
    comands_dict[comand](param)
