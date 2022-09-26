answers = ("Python3", "UTF8", "is", "2")
countTrueAnswer = 0

print("Игра в загадки\nКакая версия языка сейчас актуальна?")
user_answer = input()
if user_answer.casefold() == answers[0].casefold():
    print("Ответ " + user_answer + " верен")
    countTrueAnswer += 1
else:
    print("Неверный ответ")

print("Какая кодировка используется в строках?")
user_answer = input()
if user_answer.casefold() == answers[1].casefold():
    print("Ответ " + user_answer + " верен")
    countTrueAnswer += 1
else:
    print("Неверный ответ")

print("Какой оператор сравнения нужно использовать для работы с None и bool?")
user_answer = input()
if user_answer.casefold() == answers[2].casefold():
    print("Ответ " + user_answer + " верен")
    countTrueAnswer += 1
else:
    print("Неверный ответ")

print("Сколько значений есть у bool?")
user_answer = input()
if user_answer.casefold() == answers[3].casefold():
    print("Ответ " + user_answer + " верен")
    countTrueAnswer += 1
else:
    print("Неверный ответ")

print("Дано " + str(countTrueAnswer) + " правильных ответов")
