import codecs
import math

def summon_StopIteration():
    for elem in [0]:
        yield elem
    return 'smth'
#gen = summon_StopIteration()
#next(gen)
#next(gen)

class summon_Arithmetics_Errors(object):
    def summon_ZeroDivisionError(self):
        a = 1/0

    def summon_FloatingPointError(self):
        math.exp(1000)

    def summon_OverFlowError(self):
        math.exp(1000)

#a = summon_Arithmetics_Errors()
#a.summon_FloatingPointError()
#a.summon_ZeroDivisionError()
#a.summon_OverFlowError()

def summon_Assertion_Error():
    assert 1 == 2
#summon_Assertion_Error()

def summon_AttributeError():
    str = 'p'
    err = str.exp()
#summon_AttributeError()

def summon_Buffer_Error():
    pass

def summon_ImportError():
    import error
#summon_ImportError()

class summon_LookupError(object):
    def summon_KeyError(self):
        dict = {1:'a', 2:'b'}
        dict[3]

    def summon_IndexError(self):
        list = [0]
        list[1]

#a = summon_LookupError()
#a.summon_KeyError()
#a.summon_IndexError()

def summon_MemoryError():
    for i in list(range(999999999999999)):
        pass
#summon_MemoryError()

def summon_NameError():
    prmnt('hi')
#summon_NameError()

class summon_OSEError(object):
    def summon_FileNotFoundError(self):
        open('hh')


#a = summon_OSEError
#a.summon_FileNotFoundError(self=-1)