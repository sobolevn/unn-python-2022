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


def highlight_(code: str) -> None:
    print(highlight(code, PythonLexer(), TerminalFormatter()))


def cowsay_(text: str) -> None:
    print(cow.milk_random_cow(text))


def time_(timezone: str) -> None:
    local_date = datetime.now(pytz.timezone(timezone))
    print("{0} {1}".format(local_date.date(), local_date.time()))


def help_() -> None:
    print("EXAMPLE COMMAND:")
    print(" highlight 'any text'")
    print(" cowsay 'any text'")
    print(" time 'Region/City'")


functions = {'highlight': highlight_, 'cowsay': cowsay_, 'time': time_, 'help': help_}   # noqa: E501
