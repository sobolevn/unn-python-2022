from argparse import Namespace, _SubParsersAction  # noqa: WPS450


class Command(object):
    name: str
    help: str
    arguments: list[tuple[str, str]]

    @classmethod
    def add_to_subparsers(cls, subparsers: _SubParsersAction) -> None:
        subparser = subparsers.add_parser(cls.name, help=cls.help)
        for arg_name, arg_help in cls.arguments:
            subparser.add_argument(arg_name, help=arg_help)
        subparser.set_defaults(func=cls.perform)

    @classmethod
    def perform(cls, args: Namespace):
        raise NotImplementedError
