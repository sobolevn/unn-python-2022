success = 0
Answers_and_Questions = {"Какая версия языка сейчас актуальна?": "python3",
                         "Какая кодировка используется в строках?": "UTF8",
                         "Какой оператор сравнения нужно использовать для работы с None и bool?": "is",
                         "Сколько значений есть у bool?": 2}
for question in Answers_and_Questions:
    answer = input(question + "\nВаш ответ тут: ")
    if answer.upper() != str(Answers_and_Questions[question]).upper():
        print("Неверный ответ.")
    else:
        success += 1
        print("Ответ " + answer + " верен")

print("Количество правильных ответов: " + str(success) + "; Количество неверных ответов: " + str(4 - success) + ";")

