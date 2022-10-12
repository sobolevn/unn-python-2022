
import os, sys

from pytest import yield_fixture
# BaseException
def main():
#  +-- SystemExit
    try:
        exit()
    except SystemExit:
        print("SystemExit")
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
    def generator():
        try:
            yield 0
        except GeneratorExit:
            print("GeneratorExit")
            raise
    x = generator()
    next(x)
    x.close()
#  +-- Exception
#       +-- StopIteration
    try:
        x = iter(range(1))
        next(x)
        next(x)
    except StopIteration:
        print("StopIteration")
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
    # Not currently used
#       |    +-- OverflowError
    try:
        float(10**1000)
    except OverflowError:
        print("OverflowError")
#       |    +-- ZeroDivisionError
    try:
        1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError")
#       +-- AssertionError
    try:
        assert(False)
    except AssertionError:
        print("AssertionError")
#       +-- AttributeError
    try:
        sum.plus()
    except AttributeError:
        print("AttributeError")
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
    try:
        from pr2 import import_
    except ImportError:
        print("ImportError")
#       |    +-- ModuleNotFoundError
    try:
        from pr import import_
    except ModuleNotFoundError:
        print("ModuleNotFoundError")
#       +-- LookupError
#       |    +-- IndexError
    try:
        lst = []
        lst[1]
    except IndexError:
        print("IndexError")
#       |    +-- KeyError
    try:
        dict = {}
        dict[1]
    except KeyError: 
        print("KeyError")
#       +-- MemoryError
    try:
        s = 'Sounds bad'
        while True:
            s *= 100
    except MemoryError: 
        print("MemoryError")
#       +-- NameError
    try:
        nu_i_imechko
    except NameError:
        print("NameError")
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
    try:
        with open('smth'):
            pass
    except FileNotFoundError:
        print("FileNotFoundError")
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
    try:
        f = open("dir")
    except IsADirectoryError:
        print("IsADirectoryError")
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
    def generator():
        try:
            yield 0
        except RuntimeError:
            raise 
    x = generator()
    next(x)
    x.close()
#       |    +-- NotImplementedError
#       |    +-- RecursionError
    try:
        def error():
            error()
        error()
    except RecursionError:
        print("RecursionError")
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
    try:
        1 + 'a'
    except TypeError:
        print("TypeError")
#       +-- ValueError
    try:
        int('a')
    except ValueError:
        print("ValueError")
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
    try:
        'smth'.encode('utf-16').decode('utf-8')
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError


if __name__ == "__main__":
    main()