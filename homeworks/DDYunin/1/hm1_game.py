import random

secrets = {"Какая версия языка сейчас актуальна?":"Python3", "Какая кодировка используется в строках?":"UTF8","Какой оператор сравнения нужно использовать для работы с None и bool?":"is", "Сколько значений есть у bool?":"2" }

num_ques = 10
num_right_ans = 0

print("\nДавайте сыграем в игру загадки! Итак начнём!\n")

for i in range(num_ques):
    ki = random.choice(tuple(secrets.keys()))
    print(f"\tВопрос №{i+1}")
    print(ki)
    ans = input('Введите свой ответ: ')
    if secrets[ki].lower() == ans.lower():
        print(f"\nОтвет {ans} верен")
        num_right_ans += 1
    else:
        print("\nНеверный ответ")

print(f"\nИгра закончилась!\n\tВаша статистика:\nВсего ответов - {num_ques}\nВерных ответов - {num_right_ans}\nНеверных ответов - {num_ques - num_right_ans}")