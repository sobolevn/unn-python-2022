"""Commands file."""
import pytz
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from cowsay import ghostbusters
from datetime import datetime


def select_command(command, parametr = None):
    """
    Select command.

    Args:
        command, parametr
    """
    commands[command](parametr)


def highlight_fun(text):
    """
    Highlight text.

    Args:
        text
    """
    print(highlight(text, PythonLexer(), TerminalFormatter()))


def cowsay_ghostbusters(text):
    """
    Use ghostbusters text wrapping.

    Args:
        text
    """
    print(ghostbusters(text))


def time_fun(region):
    """
    Show the time of the specified region.

    Args:
        region
    """
    timezone = pytz.timezone(region)
    local_time = datetime.now(timezone)
    print('Time: {0}'.format(local_time.time()))


commands = {
    'highlight': highlight_fun,
    'cowsay': cowsay_ghostbusters,
    'time': time_fun,
    }
