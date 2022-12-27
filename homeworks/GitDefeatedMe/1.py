question = {
    "Какая версия языка сейчас актуальна?" : "Python3",
    "Какая кодировка используется в строках?" : "UTF8",
    "Какой оператор сравнения нужно использовать для работы с None и bool?" : "is",
    "Сколько значений есть у bool?" : "2"
}

RightAnswer = 0

for i in question:
    answer = input(i+"  ")
    if (answer.lower() == question[i].lower()):
        print("Ответ {0} верен".format(answer))
        RightAnswer+=1
        continue
    print("Неверный ответ")
print("You have {0} correct answers out of {1}" .format(RightAnswer ,len(question)))