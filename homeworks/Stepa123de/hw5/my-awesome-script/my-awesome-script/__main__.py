#__main__.py

from myinput import myinput


def main():
    myinput();

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')