y = [1, 2, 3]
x = iter(y)
x.__next__()
x.__next__()
x.__next__()
try:
    x.__next__()
except StopIteration:
    print("StopIteration")

dict = {'a' : 1, 'b' : 2}
try:
    dict[0]
except KeyError:
    print("KeyError")  


def devision(a, b):
    return a/b

try:
    devision(1, 0)
except ZeroDivisionError:
    print("ZeroDivisionError")


try:
    devision(1, 'a')
except TypeError:
    print("TypeError")

try:
    devision(10, 3)
except FloatingPointError:
    print("FloatingPointError")    


try:
    devision(1, z)
except NameError:
    print("NameError")


try:
    a = input()
    print ("Try using KeyboardInterrupt")

except KeyboardInterrupt:
    print ("KeyboardInterrupt exception")  #Ошибка возникнет, например, если нажать ctrl +c
else:
    print ("No exceptions are caught")



# IndentationError
    #if 0 == 0:
    #print('0=0')


#SyntaxError:
#numbers = [1, 2, 3]
#if 1 in numbers:
#    print('1 is number')
#    break

