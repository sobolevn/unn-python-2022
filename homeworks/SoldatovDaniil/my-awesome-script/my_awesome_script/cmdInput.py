import argparse
from commands import task


def cmd_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("todo", type=str, help="highlight 'any text' or cowsay 'any text' or time 'Region/City'")
    parser.add_argument("text", type=str, help="highligh:Text,cowsay:Text,Time: Region/City")
    args = parser.parse_args()

    try:
        task(args.todo, args.text)
    except Exception as ex:
        task("help")
        raise ex
