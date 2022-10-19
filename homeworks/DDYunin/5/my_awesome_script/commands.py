import pytz
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from cowsay import turkey
from datetime import datetime


def selected_command(command, parametr=None):
    all_commands[command](parametr)


def command_highlight(text):
    print(highlight(text, PythonLexer(), TerminalFormatter()))


def command_cowsay(phrase):
    print(turkey(phrase))


def command_time(area):
    city = pytz.timezone(area)
    local_time = datetime.now(city)
    print('Date: {0} \nTime: {1}'.format(local_time.date(), local_time.time()))


all_commands = {
    'highlight': command_highlight,
    'cowsay': command_cowsay,
    'time': command_time,
    }
