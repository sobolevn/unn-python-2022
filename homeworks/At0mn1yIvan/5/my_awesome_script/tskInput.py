import argparse
from cmnds import task, functions


def com_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Input action.",  choices=functions)
    parser.add_argument("text", help="highlight 'any text' or cowsay 'any text' or time 'Region/City'.")
    args = parser.parse_args()

    try:
        task(args.action, args.text)
    except Exception as ex:
        task("help")
        raise ex