from argparse import ArgumentParser, Namespace

from cowpy.cow import Cowacter

from pygments import highlight as hl
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

from datetime import datetime
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


def highlight(args: Namespace) -> None:
    code = args.code

    print(hl(
        code,
        PythonLexer(),
        TerminalFormatter(),
    ))


def cowsay(args: Namespace) -> None:
    phrase = args.phrase

    cow = Cowacter(eyes='stoned')
    print(cow.milk(phrase))


def time(args: Namespace) -> None:
    region = args.region

    try:
        tz = timezone(region)
    except UnknownTimeZoneError:
        print('Region is not found')
    else:
        print(datetime.now(tz).strftime('%H:%M:%S'))


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(prog='my-awesome-script')

    subparsers = parser.add_subparsers(
        required=True,
        title='subcommands',
    )

    parser_highlight = subparsers.add_parser(
        'highlight',
        help='Hightlights python code in your terminal',
    )
    parser_highlight.add_argument('code', help='The python code to highlight')
    parser_highlight.set_defaults(func=highlight)

    parser_cowsay = subparsers.add_parser(
        'cowsay',
        help='A cow will say everything you want',
    )
    parser_cowsay.add_argument('phrase', help='The phrase of a cow')
    parser_cowsay.set_defaults(func=cowsay)

    parser_time = subparsers.add_parser(
        'time',
        help='Get time of the specific region',
    )
    parser_time.add_argument('region', help='The region to get time of')
    parser_time.set_defaults(func=time)

    return parser
