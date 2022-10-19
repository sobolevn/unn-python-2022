from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from cowpy import cow
from datetime import datetime, timedelta
from pytz import timezone
import pytz


def task(todo, text):
    if todo != "help":
        functions[todo](text)
    else:
        functions[todo]()


def highlight_(text):
    print(highlight(text, PythonLexer(), TerminalFormatter()))


def cowsay_(text):
    print(cow.milk_random_cow(text))


def time_(timezone):
    local_date = datetime.now(pytz.timezone(timezone))
    print("{0} {1}".format(local_date.date(), local_date.time()))


def help_():
    print("EXAMPLE COMMAND:")
    print(" highlight 'any text'")
    print(" cowsay 'any text'")
    print(" time 'Region/City' (example: Europe/Moscow)")


functions = {"highlight": highlight_, "cowsay": cowsay_, "time": time_, "help": help_}
