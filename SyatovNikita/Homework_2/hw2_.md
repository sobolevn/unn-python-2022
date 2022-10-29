## Теория

Порядок прочтения важен!

### Материалы по Python

- Документация `tuple`: https://docs.python.org/3/library/stdtypes.html#typesseq-tuple
- Документация `list`: https://docs.python.org/3/tutorial/datastructures.html
- Документация `dict`: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- `tuple` vs `list`: http://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each http://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples http://nedbatchelder.com/blog/201608/lists_vs_tuples.html
- `dict`: https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
- Что такое функция? https://www.tutorialspoint.com/python/python_functions.htm
- Что значит - вызвать функцию? https://stackoverflow.com/questions/19130958/what-does-it-mean-to-call-a-function-in-python
- Что такое `*args` и `**kwargs`: https://lancelote.gitbooks.io/intermediate-python/content/book/args_and_kwargs.html

### Материалы для продвинутых

- Что такое хеш-таблицы? https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D1%88-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0
- Какие бывают списки? https://en.wikipedia.org/wiki/Linked_list#Linked_lists_vs._dynamic_arrays
- Как устроен список внутри? https://www.quora.com/How-are-Python-lists-implemented-internally
- Что такое `Sequence`: https://docs.python.org/3/library/stdtypes.html#typesseq
- Что такое `Iterable`: https://docs.python.org/3/glossary.html#term-iterable
- Сложность операций: https://wiki.python.org/moin/TimeComplexity
- Modern dictionaries (from Python Core developer): https://www.youtube.com/watch?v=p33CVV29OG8

### ООП в целом

- Начальный уровень теории: https://habrahabr.ru/post/87119/
- Принципы ООП: https://habrahabr.ru/post/87205/

### ООП и Python

- Основы: https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html
- Примеры использования: http://snakeproject.ru/rubric/article.php?art=python_oop
- Большая теоритическая статья: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
- Магические методы: https://rszalski.github.io/magicmethods/

### Критика

- Почему в некоторых случаях не нужен ООП: https://habrahabr.ru/post/140581/
- Сомнение в принципах ООП: https://habrahabr.ru/post/147927/

### Детали реализации

- super: http://pythonicway.com/education/python-oop-themes/21-python-inheritance и https://www.youtube.com/watch?v=EiOglTERPEo
- Магические методы: https://habrahabr.ru/post/186608/
- class attributes vs instance attributes: http://stackoverflow.com/questions/207000/python-difference-between-class-and-instance-attributes


## Практика

Написать свой собственный класс "списков", который мы назовем `Array`.

Что должен делать уметь ваш `Array`?

- Создавать себя как на примере: `Array()` - пустой списо, `Array(1)` = список из одного объекта `1`, `Array(1, 2, 3)` - список из трех объектов. `Array` должен уметь работать с любым количеством аргументов
- Добавлять новый объект внутрь списка через метод `.append()`
- Складываться с другими `Array`. Например: `Array(1) + Array(2) == Array(1, 2)`
- Узнавать свою длину через функцию `len()`
- Находить индекс переданного объекта через метод `.index()`, возвращаем `-1`, если такого объекта в списке нет. Например: `Array('a', 'b').index('b') == 1`
- Работать с циклом `for`: `for element in Array(1, 2, 3):`
- Получать значение по индексу при помощи `[]`. Пример: `Array('a')[0] == 'a'`

Требования:

- Хранить состояние `Array` в свойстве `self._data`, использовать `tuple`
- Наследоваться нужно и можно только от `object`
