from itertools import accumulate
from inspect import getsource
import re

EMPTY_STRING = ""
def map_and_str(format_fun, elements, firstChar='[', lastChar=']'):
    strIterable = ', '.join(map(format_fun, elements))
    return firstChar+strIterable+lastChar

def function_to_str(function):
    if function==None:
        return None
    try:
        # patt = re.compile(r'\b(' + '|'.join(function.__dict__.keys()) + r')\b')
        # s = patt.sub(lambda x: function.__dict__[x.group()] if x.group in function.__dict__ else '', getsource(function))
        # return s
        return getsource(function)
    except OSError:
        return function.__name__
    except TypeError:
        try:
            # patt = re.compile(r'\bself.(' + '|'.join(function.__dict__.keys()) + r')\b')
            # selfpatt = re.compile(r'^self.')
            # s = patt.sub(lambda x: str(function.__dict__[selfpatt.sub('',x.group())]), getsource(function.__call__))
            # return s
            return getsource(function.__call__)
        except:
            raise
        
def print_and_wait(x):
    print(x)
    input("Press Enter...")
    
def sort_using_2nd_list(elements, sortingKeys):
    mergedList = zip(elements, sortingKeys)
    sortedLists = sorted(mergedList, key=lambda x: x[1])
    sortedElements = type(elements)(a for a,b in sortedLists)
    sortedKeys = type(sortingKeys)(b for a,b in sortedLists)
    return (sortedElements, sortedKeys)
    
def get_best(elements, keyList=None, minimization=False):
    mergedList = zip(elements, keyList)
    if minimization==True:
        bestElement = min(mergedList, key=lambda x: x[1])[0]
    else:
        bestElement = max(mergedList, key=lambda x: x[1])[0]
    return bestElement
    
def normalize(aList):
    positiveList = add_offset_for_positive_values(aList)
    return type(aList)(elem/sum(positiveList) for elem in positiveList)
    
def add_offset_for_positive_values(aList):
    if min(aList) >= 0:
        return aList
    else:
        offset = min(aList)
        return type(aList)(elem-offset for elem in aList)

def accumulate_sums(aList):
    return type(aList)(accumulate(aList))
    
def isinset(subset, superset):
    sub=set(subset)
    super=set(superset)
    return sub<=super

def compare_iterables_by_element(iter1, iter2):
    iter1, iter2 = iter(iter1), iter(iter2)
    for elem1 in iter1:
        try:
            elem2 = next(iter2)
        except StopIteration:  #len(iter2)>len(iter1)
            return False
        if elem1!=elem2:  #iter1[i]!=iter2[i]
            return False
    try:
        next(iter2)
    except StopIteration:  #len(iter2)==len(iter1)
        return True        

    return False  #len(iter2)<len(iter1)

