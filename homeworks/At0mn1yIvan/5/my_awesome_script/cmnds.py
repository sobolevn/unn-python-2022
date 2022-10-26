from datetime import datetime

import pytz
from cowpy import cow
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


def task(action: str, text: str = None) -> None:
    if action == 'help':
        functions[action]()
    else:
        functions[action](text)


def Highlight(code: str) -> None:
    print(highlight(code, PythonLexer(), TerminalFormatter()))


def Cowsay(text: str) -> None:
    print(cow.milk_random_cow(text))


def Time(timezone: str) -> None:
    local_date = datetime.now(pytz.timezone(timezone))
    print("{0} {1}".format(local_date.date(), local_date.time()))


def Help() -> None:
    print("EXAMPLE COMMAND:")
    print(" highlight 'any text'")
    print(" cowsay 'any text'")
    print(" time 'Region/City'")


functions = {'highlight': Highlight, 'cowsay': Cowsay, 'time': Time, 'help': Help}   # noqa: E501
