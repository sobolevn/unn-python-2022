from cowpy import cow
import pytz
import datetime as dt
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
text = None
cheese = None
msg = None
timezone_nw = None
nw_datetime_obj = None
timezone_new = None
new_datetime_obj = None
while True:
    command = str(input(">>>"))
    if command == "my-awesome-script highligh":
        text = str(input("Введите текст для подсветки: "))
        lexer = PythonLexer()
        formatter = TerminalFormatter()
        result = highlight(text, lexer, formatter)
        print(result)
    elif command == "my-awesome-script cowsay":
        text = str(input("Введите текст для обрамления: "))

        cheese = cow.Moose(thoughts=True)
        msg = cheese.milk(text)
        print(msg)

        cheese = cow.Moose(thoughts=True, tongue=True, eyes='dead')
        msg = cheese.milk(text)
        print(msg)
    elif command == "my-awesome-script time":
        text = str(input("Введите данные на английском в следующем формате "
                         "Часть света/Город (пример Europe/Moscow): "))
        try:
            timezone_nw = pytz.timezone('America/New_York')
            nw_datetime_obj = dt.datetime.now(timezone_nw)
            timezone_new = pytz.timezone(text)
            new_datetime_obj = nw_datetime_obj.astimezone(timezone_new)
            print(text, ':', new_datetime_obj)
        except Exception:
            print("Введены некорректные данные!")
    elif command == "exit()":
        exit()
    elif command == "my-awesome-script --help":
        print("command #1 - my-awesome-script highligh; parameters: "
              "text= {0}".format(text))
        print("command #2 - my-awesome-script cowsay; parameters: "
              "text= {0}, cheese= {1}, msg= {2}".format(text, cheese, msg))
        print(
            "command #3 - my-awesome-script time; parameters: "
            "text= {0}, timezone_nw= {1}, nw_datetime_obj= {2}, "
            "timezone_new= {3}, new_datetime_obj= {4}".format(
                text, timezone_nw, nw_datetime_obj,
                timezone_new, new_datetime_obj))
        print("command #4 - exit()")
    else:
        print(f"\"{command}\" не является внутренней или внешней командой,"
              f"исполняемой программой или пакетным файлом.")


'''На заметку:
        основа: ---timezone_nw = pytz.timezone('America/New_York')
        nw_datetime_obj = dt.datetime.now(timezone_nw) ---
        timezone_london = pytz.timezone('Europe/London')
        london_datetime_obj = nw_datetime_obj.astimezone(timezone_london)
        print('America/New_York:', nw_datetime_obj)
        print('Europe/London:', london_datetime_obj)

        timezone_mscw = pytz.timezone('Europe/Moscow')
        mscw_datetime_obj = nw_datetime_obj.astimezone(timezone_mscw)
        print('Europe/Moscow:', mscw_datetime_obj)

        timezone_ams = pytz.timezone('Europe/Amsterdam')
        ams_datetime_obj = nw_datetime_obj.astimezone(timezone_ams)
        print('Europe/Amsterdam:', ams_datetime_obj)'''
