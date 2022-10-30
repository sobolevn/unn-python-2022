from todo.commands import BaseCommand
from todo.custom_exceptions import UserExitException
from todo.reflection import find_classes
from todo.storage import Storage


def get_routes() -> dict:
    routes = find_classes(BaseCommand)
    return {
        route().label: route
        for _, route in routes
    }


def perform_command(command: str) -> None:
    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
    except KeyError:
        print('Bad command, try again.')
        return

    command_inst = command_class()
    storage = Storage()

    try:
        command_inst.perform(storage)
    except UserExitException as ex:
        # Handling `exit` command.
        print(ex)
        raise


def parse_user_input():
    commands = get_routes().keys()
    message = 'Input your command: ({0}): '.format('|'.join(commands))
    return input(message)


