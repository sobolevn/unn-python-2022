from typing import Final

from my_awesome_script.parser import create_parser

PROG_NAME: Final = 'my_awesome_script'


def main() -> None:
    parser = create_parser(PROG_NAME)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
