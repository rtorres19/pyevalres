import itertools

EMPTY_STRING = ""
def turn_iterable_to_string_using(elements, format_fun):
    numberOfElements = len(elements)
    if numberOfElements==0:
        return "[]"
    
    formattedString = EMPTY_STRING
    for i in range(numberOfElements):
        element = elements[i]
        formattedElement = format_fun(element)
        readyToConcat = give_list_format(formattedElement, i, numberOfElements)
        formattedString += readyToConcat
        
    return formattedString
    
def give_list_format(stringToFormat, positionInList, numberOfElements):
    if numberOfElements == 0:
        return "[]"
        
    last = numberOfElements - 1
    
    if positionInList == 0:
        beginOfString = "["
    else:
        beginOfString = ", "
        
    if positionInList == last:
        endOfString = "]"
    else:
        endOfString = ""
        
    return beginOfString + stringToFormat + endOfString
    
def print_and_wait(x):
    print(x)
    input("Press Enter...")
    
def merge_sort_and_unpack_using_2nd_list(elements, sortingKeys):
    mergedList = list(zip(elements, sortingKeys))
    mergedList.sort(key=lambda x: x[1])
    for i in range(len(elements)):
        elements[i] = mergedList[i][0]
        sortingKeys[i] = mergedList[i][1]
        
def get_best(elements, keyList):
    mergedList = list(zip(elements, keyList))
    bestElement = max(mergedList, key=lambda x: x[1])[0]
    return bestElement
    
def normalize(aList):
    acum = 0
    for elem in aList:
        acum += elem
    return [elem/acum for elem in aList]
    
def add_offset_for_positive_values(aList):
    offset = min(aList)
    if offset >= 0:
        return aList
    else:
        return [elem+offset for elem in aList]
        
def accumulate_sums(aList):
    return list(itertools.accumulate(aList))
    
def isinset(subset, superset):
    sub=set(subset)
    super=set(superset)
    return sub<=super