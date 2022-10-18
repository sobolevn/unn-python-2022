from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from cowpy import cow
from datetime import datetime
import pytz


def highligh(text: str):
    print(highlight(text, PythonLexer(), TerminalFormatter()))


def cowsay(text: str):
    print(cow.milk_random_cow(text))


def time(timezone):
    local_date = datetime.now(pytz.timezone(timezone))
    print("{0} {1}".format(local_date.date(), local_date.time()))
