"""Commands for the script."""

from datetime import datetime

from cowpy.cow import Cowacter
from pygments import highlight as hl
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
from pytz import timezone


def run_command(command: str):
    """
    Select command.

    Args:
        command: command name

    Returns:
        :return: selected command
    """
    return commands[command]


def highlight(code: str):
    """
    Highlight code.

    Args:
        code: code to highlight
    """
    this_lexer = get_lexer_by_name('python')
    this_formatter = get_formatter_by_name('html')
    print(hl(code, lexer=this_lexer, formatter=this_formatter))  # noqa: WPS421


def cowsay(text: str):
    """
    Make the cow talk.

    Args:
        text: text that the cow say
    """
    cow = Cowacter()
    print(cow.milk(text))  # noqa: WPS421


def time(region: str):
    """
    Show time in the region.

    Args:
        region: selected region
    """
    ftime = '%H:%M:%S'
    time_zone = timezone(region)
    print(datetime.now(time_zone).strftime(ftime))  # noqa: WPS421


commands = {'highlight': highlight, 'cowsay': cowsay, 'time': time}
