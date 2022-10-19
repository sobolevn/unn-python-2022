import argparse

from pygments import highlight
from pygments.style import Style
from pygments.token import Token
from pygments.lexers import Python3Lexer
from pygments.formatters import Terminal256Formatter

from cowpy import cow

from datetime import datetime
from pytz import timezone



def input_from_cmd():
    parser = argparse.ArgumentParser(description = "my_awesome_script highlights the syntax and outputs the time")
    parser.add_argument("command", type = str, help = "input command", choices=["highlight", "cowsay", "time"])
    parser.add_argument("text", type = str, help = "input text")
    args = parser.parse_args()
    
    commands[args.command](args.text)

def _highlight(text :str):
    print(highlight(text, Python3Lexer(), Terminal256Formatter(style='colorful')))

def _cowsay(text :str):
    print(cow.milk_random_cow(text))

def _time(region :str):
    fmt = '%Y-%m-%d %H:%M:%S'
    print(datetime.now(timezone(region)).strftime(fmt))

commands = {"highlight": _highlight, "cowsay":_cowsay, "time": _time}
