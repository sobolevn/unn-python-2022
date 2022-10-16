from argparse import ArgumentParser, Namespace

from pygments import highlight as hl
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


def highlight(args: Namespace) -> None:
    print(hl(
        args.code,
        PythonLexer(),
        TerminalFormatter(),
    ))


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
    parser_highlight.add_argument('code', help='Python code to highlight')
    parser_highlight.set_defaults(func=highlight)

    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
