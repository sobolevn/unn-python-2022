from colorama import Fore
import pytz
from datetime import datetime
import argparse
from cowpy import cow


def main():
    def animal(text):
        cheese = cow.DragonAndCow()
        msg = cheese.milk(text)
        print(msg)

    def color(text):
        print(Fore.RED + text)

    def dttime(timezone):
        ist_time = pytz.timezone(timezone)
        print(datetime.now(tz=ist_time))

    parser = argparse.ArgumentParser()
    parser.add_argument('-cs','--cowsay', help="Creates an animal with your text", default=None)
    parser.add_argument('-hl','--highligh', help="Highlights your text", default=None)
    parser.add_argument('-tm','--time', help="Shows the time In the selected time zone", default=None,
                        choices=['Europe/Warsaw', 'America/Nuuk', 'America/Vancouver', 'Antarctica/Mawson',
                                 'Atlantic/South_Georgia'])
    args = parser.parse_args()
    if args.cowsay != None:
        animal(args.cowsay)
    if args.highligh != None:
        color(args.highligh)
    if args.time != None:
        dttime(args.time)


if __name__ == '__main__':
    main()