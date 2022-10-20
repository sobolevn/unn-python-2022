from argparse import Namespace
from datetime import datetime

from cowpy.cow import Cowacter
from pygments import highlight as hl
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

from my_awesome_script.classes import Command


class HighlightCommand(Command):
    name = 'highlight'
    help = 'Hightlights python code in your terminal'
    arguments = [('code', 'The python code to highlight')]

    @classmethod
    def perform(cls, args: Namespace):
        code = args.code

        print(hl(
            code,
            PythonLexer(),
            TerminalFormatter(),
        ))


class CowsayCommand(Command):
    name = 'cowsay'
    help = 'A cow will say everything you want'
    arguments = [('phrase', 'The phrase of a cow')]

    @classmethod
    def perform(cls, args: Namespace):
        phrase = args.phrase

        cow = Cowacter(eyes='stoned')
        print(cow.milk(phrase))


class TimeCommand(Command):
    name = 'time'
    help = 'Get time of the specific region'
    arguments = [('region', 'The region to get time of')]

    @classmethod
    def perform(cls, args: Namespace):
        region = args.region

        try:
            tz = timezone(region)
        except UnknownTimeZoneError:
            print('Region is not found')
        else:
            print(datetime.now(tz).strftime('%H:%M:%S'))
