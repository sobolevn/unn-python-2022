import argparse
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from cowpy import cow
from datetime import datetime
import pytz

def highligh_func(text: str):
    print(highlight(text, PythonLexer(), TerminalFormatter()))


def cowsay(text: str):
    print(cow.milk_random_cow(text))


def time(timezone):
    local_date = datetime.now(pytz.timezone(timezone))
    print("{0} {1}".format(local_date.date(), local_date.time()))

def main():
    parse_input()

comands_dict = {'highlight': highligh_func, 'cowsay': cowsay, 'time': time}


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', type=str,
                        choices=['highlight', 'cowsay', 'time'],
                        help='Enter comand from this list'
                        )
    parser.add_argument('param', type=str,
                        help='''Enter <text> for highlight or cowsay,
                        or <Region/City> for time'''
                        )
    args = parser.parse_args()
    use_comand(args.operation, args.param)


def use_comand(comand, param):
    comands_dict[comand](param)

if __name__ == '__main__':
    main()