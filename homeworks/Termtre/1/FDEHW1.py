success = 0
answer = input("Какая версия языка сейчас актуальна?\nВаш ответ тут: ")
if str.lower(answer) != "python3":
    print("Неверный ответ.")
else:
    print("Ответ {", answer, "} верен")
    success += 1

answer = input("Какая кодировка используется в строках?\nВаш ответ тут: ")
if str.upper(answer) != "UTF8":
    print("Неверный ответ.")
else:
    print("Ответ {", answer, "} верен")
    success += 1

answer = input("Какой оператор сравнения нужно использовать для работы с None и bool?\nВаш ответ тут: ")
if str.lower(answer) != "is":
    print("Неверный ответ.")
else:
    print("Ответ {", answer, "} верен")
    success += 1

answer = input("Сколько значений есть у bool?\nВаш ответ тут: ")
if answer != "2":
    print("Неверный ответ.")
else:
    print("Ответ {", answer, "} верен")
    success += 1

print("Количество правильных ответов: " + str(success) + "; Количество неверных ответов: " + str(4 - success) + ";")
