"""
Author : Timur Poletaev
Created : 18.09.2022
Updated : -
"""
def solve():
    # я не знаю почему их тут 4, а не 10, но предположим, что кто-то когда-то туда их добавит
    ans = {
        "Какая версия языка сейчас актуальна?": "Python3",
        "Какая кодировка используется в строках?": "UTF8",
        "Какой оператор сравнения нужно использовать для работы с None и bool?": "is",
        "Сколько значений есть у bool?": "2"
    }
    print("Викторина от Тимура Полетаева")
    counter = 0
    for question, answer in ans.items():
        user_answer = input(question)
        if user_answer.lower() == answer.lower():
            print(f"Ответ '{user_answer}' верен")
            counter += 1
        else:
            print("Неверный ответ.")
    print(f"Набрано баллов : {counter}/{len(ans)}")
