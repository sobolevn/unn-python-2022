import random
# A game of riddles:

count = 0
n = 10
questions = ('Какая версия языка сейчас актуальна?', 'Какая кодировка используется в строках?', 
'Какой оператор сравнения нужно использовать для работы с None и bool?', 'Сколько значений есть у bool?')
ansvers = ('Python3', 'UTF8', 'is', '2')


for i in range(n):
    j = random.randint(0,3)
    print(questions[j])
    users_input = str(input('Введите ответ: '))
    if users_input.lower() == ansvers[j].lower() :
        count+=1
        print("Ответ {0} верен".format(users_input))
    else:
        print("Ответ неверный\n")

print('Число отгаданных загадок: {0} из 10'.format(count))

