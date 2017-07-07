from Utility import *
import random

emptyList = []
aList = [1, 2, 3, 4]
aListString="[1, 2, 3, 4]"
stringTested="a"
unsortedHello = ["l","o","\n","e","h","l"]
unsortedHelloOrder = [3,5,6,2,1,4]
nonAcumulatedList = [1,0,2,5,0,10]
acumulatedSumList = [1,1,3,8,8,18]
sortedHello = ["h","e","l","l","o","\n"]

def turn_iterable_to_string_using_test():
    stringResult = turn_iterable_to_string_using(aList, str)
    assert(stringResult==aListString)
    stringResult = turn_iterable_to_string_using(emptyList, str)
    assert(stringResult=="[]")

def give_list_format_test():
    empty_list_format_test()
    single_element_list_format_test()
    multiple_element_list_format_test()
    assert(True)
    
def empty_list_format_test():
    numberOfElements = 0
    position = random.randint(0,10)
    formattedString = give_list_format(stringTested, position, numberOfElements)
    assert(formattedString=="[]")

def single_element_list_format_test():
    numberOfElements = 1
    position = 0
    formattedString = give_list_format(stringTested, position, numberOfElements)
    assert(formattedString=="[a]")
    
def multiple_element_list_format_test():
    numberOfElements = len(aList)
    position = range(0, numberOfElements)
    formattedList = EMPTY_STRING
    for i in position:
        formattedString = give_list_format(str(aList[i]), i, numberOfElements)
        formattedList += formattedString
    assert(formattedList==aListString)
    
def merge_sort_and_unpack_using_2nd_list_test():
    a = unsortedHello
    b = unsortedHelloOrder
    merge_sort_and_unpack_using_2nd_list(a, b)
    assert(a==sortedHello and b==list(range(1,7)))
    
def get_best_test():
    a = unsortedHello
    b = unsortedHelloOrder
    maxA = get_best(a, b)
    assert(maxA=="\n")
    
def accumulate_test():
    a = nonAcumulatedList
    b = accumulate_sums(a)
    assert(b==acumulatedSumList)
    
    