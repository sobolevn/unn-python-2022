import argparse
from .command import command


def cmd_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", help="highlight 'any text' or cowsay 'any text' or time 'Region/City'"
                                          "(example: Europe/Moscow)",
                        choices=["highlight", "cowsay", "time"])
    parser.add_argument("text")
    args = parser.parse_args()

    try:
        command(args.operation, args.text)
    except Exception as ex:
        command("help")
        raise ex
