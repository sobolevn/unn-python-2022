import inspect
from argparse import ArgumentParser, _SubParsersAction  # noqa: WPS450
from importlib import import_module

from my_awesome_script.classes import Command


def get_commands():
    module_members = inspect.getmembers(
        import_module('.commands', 'my_awesome_script'),
    )
    commands = []
    for _, module_member in module_members:
        if not inspect.isclass(module_member):
            continue
        if module_member is not Command and issubclass(module_member, Command):
            commands.append(module_member)
    return commands


def init_commands(subparsers: _SubParsersAction):
    commands = get_commands()
    for command in commands:
        command.add_to_subparsers(subparsers)


def create_parser(prog_name) -> ArgumentParser:
    parser = ArgumentParser(prog=prog_name)

    subparsers = parser.add_subparsers(
        required=True,
        title='commands',
    )

    init_commands(subparsers)

    return parser
