from sys import exit
import numpy as np

def error_system_exit():
    try:
        exit(45)
    except SystemExit as e:
        print(f'Exit code: {e.code}')

def error_keyboard_interrupt():
    try:
        var = input()
    except KeyboardInterrupt:
        print("KeyboardInterrupt exception is caught") # ctrl + c

def error_generator_exit():
    def generate():
        values = [1, 2]
        for value in values:
            try:
                yield value
            except GeneratorExit as e:
                print('GeneratorExit Error')
                raise  # Повторно поднимаем исключение.
    my_generator = generate()
    print(next(my_generator))  # 1
    my_generator.close()  # Принудительная остановка

def error_stop_iteration():
    def generate():
        for value in [1]:
            yield value
        return 'some'

    my_generator = generate()

    next(my_generator)  # 1
    try:
        next(my_generator)  # StopIteration: some
    except StopIteration:
        print("StopIteration Error")

def error_zero_division():
    try:
        e = 20 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError!")

def error_oveerflow():
    import math
    try:  
        print(math.exp(1000))
    except OverflowError:  
        print("Исключение OverFlow.")

def error_assertion():
    try:  
        a = 100
        b = "PythonRu"
        assert a == b
    except AssertionError:  
        print("Исключение AssertionError.")

def error_attribute():
    class Attributes(object):
        a = 2
        print(a)
    try:
        obj = Attributes()
        print(obj.attribute)
    except AttributeError:
        print("Исключение AttributeError.")

def error_module_not_found():
    try:
        import sadjksljd.py
    except ModuleNotFoundError:
        print("ModuleNotFoundError")

def error_import():
    try:
        from os import dfsd
    except ImportError:
        print("It is import error!")

def error_index():
    lst = list(range(3))
    try:
        lst[51]
    except IndexError:
        print("IndexError")

def error_key():
    dictionary = {1:"Hello", 2:"World"} 
    try:
        dictionary[3]
    except KeyError:
        print("KeyError")

def error_name():
    n = 100
    try:
        s = string(n)
    except NameError:
        print("NameError")

def error_unbound_local():
    x = 10
    def sum():
        x = x + 5
        print(x)
    try:
        sum()
    except UnboundLocalError:
        print("UnboundLocalError")

def error_os():
    path = '"d:\\in put.txt"'
    try:
        fin = open(path, 'r', encoding='utf-8')
    except OSError:
        print("It is OSError")

def error_file_exists():
    try:
        redak = open("temp.txt", "x")
    except FileExistsError:
        print("It is FileExistError")

def error_file_not_found():
    import os 
    try: 
        os.remove('C:/workspace/python/data.txt') 
    except FileNotFoundError: 
        print('It is FIleNotFoundError')

def error_memory():
    try:
        np.arange(1e10)
    except MemoryError:   #not catch...
        print("It is a MemoryError")

def error_permission():
    try:
        open("D:\Programming_YuninDD\Python_course_NNGU")
    except PermissionError:
        print("It is PermissionError")

def error_not_a_directory():
    import os
    try:
        os.listdir("D:\Programming_YuninDD\Python_course_NNGU\Homework\Hm1\hm1_game.py")
    except NotADirectoryError:
        print("It is NotADirectoryError")

def error_not_implemented():
    class BaseClass(object):
        def __init__(self):
            super(BaseClass, self).__init__()
        def do_something(self):
	    # функция ничего не делает
            raise NotImplementedError(self.__class__.__name__ + '.do_something')

    class SubClass(BaseClass):
        """Реализует функцию"""
        def do_something(self):
            # действительно что-то делает
            print(self.__class__.__name__ + ' что-то делает!')

    SubClass().do_something()
    try:
        BaseClass().do_something()
    except NotImplementedError:
        print("It is NotImplementedError")

def error_recursion():
    try:
        error_recursion()
    except RecursionError:
        print("It is RecursionError")

def error_syntax():
    try:
        print("Hello") #убрать скобки у print
    except SyntaxError:
        print("It is SyntaxError")

def error_indentation():
    try:
        a = 5
            # b = 10
    except IndentationError:
        print("It is IndentationError")

def error_type():
    try:
        a = 5 + 'b'
    except TypeError:
        print("It is TypeError")

def error_value():
    string = "hello"
    try:
        number = int(string)
    except ValueError:
        print("It is ValueError")

def error_unicode_decode():
    u = 'é'
    try:
        print("ASCII Representation of é: ", u.encode('ascii'))
    except UnicodeEncodeError:
        print("It is UnicodeEncodeError")
        
error_unicode_decode()
error_value()
error_type()
error_indentation()
error_syntax()
error_recursion()
error_not_implemented()
error_not_a_directory()
error_permission()
error_file_not_found()
error_file_exists()
error_os()
error_generator_exit()
error_stop_iteration()
error_zero_division()
# error_keyboard_interrupt()
error_system_exit()
error_oveerflow()
error_assertion()
error_attribute()
error_module_not_found()
error_index()
error_key()
error_name()
error_unbound_local()
error_import()
error_memory()