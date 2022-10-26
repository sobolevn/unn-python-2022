import argparse

from cmnds import functions, task


def com_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='Input action.',  choices=functions)
    parser.add_argument('text', help="highlight 'any text'/cowsay 'any text'/time 'Region/City'")  # noqa: E501
    args = parser.parse_args()

    try:
        task(args.action, args.text)
    except Exception as ex:
        task('help')
        raise ex
