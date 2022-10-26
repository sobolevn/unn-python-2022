from tskInput import com_input


def main():
    try:
        com_input()
    except Exception as ex:
        print("Something went wrong.", ex)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
