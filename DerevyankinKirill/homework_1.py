print('Игра в загадки')
count=0
print('Загадка 1\nКакая версия языка сейчас актуальна?')
answer1=input()
if 'Python3' in answer1 or 'python3' in answer1:
    print('Ответ',answer1, 'верен')
    count=1
else:
    print('Неверный ответ')
print('Загадка 2\nКакая кодировка используется в строках?')
answer2=input()
if 'UTF8' in answer2 or 'utf8' in answer2:
    print('Ответ',answer2, 'верен')
    count=count+1
else:
    print('Неверный ответ')
print('Загадка 3\nКакой оператор сравнения нужно использовать для работы с None и bool?')
answer3=input()
if 'Is' in answer3 or 'is' in answer3:
    print('Ответ',answer3, 'верен')
    count=count+1
else:
    print('Неверный ответ')
print('Загадка 4\nСколько значений есть у bool?')
answer4=input()
if '2' in answer4:
    print('Ответ',answer4, 'верен')
    count=count+1
else:
     print('Неверный ответ')
print('Ваши ответы',count,'/4')
