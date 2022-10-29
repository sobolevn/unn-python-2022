import math
counter = 0
try:
    counter+=1
    a=1/0
except(ZeroDivisionError):
    print(f"{counter}. ZeroDivisionError")
try:
    counter+=1
    dictionary ={'Пи':3.14,'e':2.71, 'рад':57.29}
    a = dictionary['е']
except(KeyError):
    print(f"{counter}. KeyError")
try:
    counter+=1
    a = [1,2,4,3,1]
    b = a[5]
except(IndexError):
    print(f"{counter}. IndexError")
try:
    counter+=1
    a = [1,2]
    it = iter(a)
    while True:
        b = it.__next__()
except(StopIteration):
    print(f"{counter}. StopIteration")
try:
    counter+=1
    a = "Hi,world"
    a+=7
except(TypeError):
    print(f"{counter}. TypeError")
try:
    counter+=1
    print("Press Ctrl+C. Only in console")
    get_value = input()
except(KeyboardInterrupt):
    print(f"{counter}. KeyboardInterrupt")
try:
    counter+=1
    math.sqrt(-42)
except(ValueError):
    print(f"{counter}. ValueError")
try:
    counter+=1
    import sanctioned_goods
except(ImportError):
    print(f"{counter}. ImportError")
try:
    a = b
except(NameError):
    print(f"{counter}. NameError")
"""try:
    a = [3,5]
    while True:
        while True:
            a.append(9876543210123)
except(MemoryError):
    print(f"MemoryError")"""

a = input()


