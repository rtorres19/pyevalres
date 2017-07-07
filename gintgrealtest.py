from GTypes import *
import random
import GDefaults

def gint_default_creation_test():
    for i in range(100000):
        defaultInt = GInt()
        assert(hasIntDefaults(defaultInt))
        assert(defaultInt.isininterval(defaultInt.value))

def hasIntDefaults(gInt):
    return gInt.min==GDefaults.GIntMin and gInt.max==GDefaults.GIntMax
    
def gint_value_set_in_creation_test():
    value=5
    valueSetInt = GInt(value)
    assert(hasIntDefaults(valueSetInt))
    assert(valueSetInt.value==value)
    
def gint_interval_set_in_creation_test():
    min=1
    max=20
    intervalSetInt = GInt(min=min, max=max)
    assert(intervalSetInt.min==min and intervalSetInt.max==max)
    assert(intervalSetInt.isininterval(intervalSetInt.value))
    
def gint_all_set_in_creation_test():
    value=5
    min=0
    max=7
    allSetInt = GInt(value, min, max)
    assert(allSetInt.min==min and allSetInt.max==max)
    assert(allSetInt.value==value)
    wrongValue = 10
    try:
        wrongValueInt = GInt(wrongValue, min, max)
    except OverflowError:
        pass
    except:
        raise
    else:
        raise AssertionError
    
def interval_respected_test():
    one_to_a_hundred = range(1,100+1)
    b = [random.randint(i+1,200) for i in one_to_a_hundred]
    for i in one_to_a_hundred:
        lowerBound = i
        upperBound = b[i-1]
        newInt = GInt(min=lowerBound, max=upperBound)
        newReal = GReal(min=lowerBound, max=upperBound)
        assert(newInt.isininterval(newInt.value))
        assert(newReal.isininterval(newReal.value))
    
def greal_default_creation_test():
    for i in range(100000):
        defaultReal = GReal()
        assert(hasRealDefaults(defaultReal))
        assert(defaultReal.isininterval(defaultReal.value))

def hasRealDefaults(gReal):
    return gReal.min==GDefaults.GRealMin and gReal.max==GDefaults.GRealMax

def greal_value_set_in_creation_test():
    value=5.4
    valueSetReal = GReal(value)
    assert(hasRealDefaults(valueSetReal))
    assert(valueSetReal.value==value)
    
def greal_interval_set_in_creation_test():
    min=1
    max=20
    intervalSetReal = GReal(min=min, max=max)
    assert(intervalSetReal.min==min and intervalSetReal.max==max)
    assert(intervalSetReal.isininterval(intervalSetReal.value))

def greal_all_set_in_creation_test():
    value=5.1
    min=0
    max=7
    allSetReal = GReal(value, min, max)
    assert(allSetReal.min==min and allSetReal.max==max)
    assert(allSetReal.value==value)
    wrongValue = 10
    try:
        wrongValueReal = GReal(wrongValue, min, max)
    except OverflowError:
        pass
    except:
        raise
    else:
        raise AssertionError
    
def gint_assignment_test():
    gint=GInt()
    newValue=10
    gint.value=newValue
    assert(gint.value==newValue)