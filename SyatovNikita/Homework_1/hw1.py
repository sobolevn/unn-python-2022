questions = ("Какая версия языка сейчас актуальна?",
             "Какая кодировка используется в строках?",
             "Какой оператор сравнения нужно использовать для работы с None и bool?",
             "Сколько значений есть у bool?")
answers = ("Python3", "UTF8", "is", "2")
count_correct_answer = 0

for number_question in range(0, len(questions)):
    user_answer = input(questions[number_question])
    if user_answer.casefold() == answers[number_question].casefold():
        print("Ответ " + user_answer + " верен")
        count_correct_answer += 1
    else:
        print("Неверный ответ")

print("Дано " + str(count_correct_answer) + " правильных ответов")
