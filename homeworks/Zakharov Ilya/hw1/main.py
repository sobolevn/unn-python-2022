x = int(0)
answer = input("Какая версия языка сейчас актуальна? ")
if answer.upper() == 'PYTHON3':
    print("ответ " + answer + " верен")
    x = x + 1
else:
    print("неверный ответ")

answer = input("Какая кодировка используется в строках? ")
if answer.upper() == 'UTF8':
    print("ответ " + answer + " верен")
    x = x + 1
else:
    print("неверный ответ")

answer = input("Какой оператор сравнения нужно использовать для работы с None и bool? ")
if answer.upper() == 'IS':
    print("ответ " + answer + " верен")
    x = x + 1
else:
    print("неверный ответ")

answer = input("Сколько значений есть у bool? ")
if answer.upper() == '2':
    print("ответ " + answer + " верен")
    x = x + 1
else:
    print("неверный ответ")

print("было дано 4 ответа, правильно из них", x)