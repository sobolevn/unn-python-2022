

questions = ["Какая версия языка сейчас актуальна?",
             "Какая кодировка используется в строках?",
             "Какой оператор сравнениянужноиспользоватьдляработысNoneиbool?",
             "Сколько значений есть у bool?"]
answers = ["Python3", "UTF8", "is", "2"]

goal = 0  # количество правильных ответов

for i in range(0, len(questions)):
    print(questions[i])
    res = input("Введите ответ: ").lower()
    if res == answers[i].lower():
        print(f"Ответ {answers[i]} верен")
        goal += 1
    else:
        print("Неверный ответ")


print(f"Количество правильных ответов {goal}")
