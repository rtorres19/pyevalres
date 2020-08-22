import unittest
from Utility import *
import random

class TestUtility(unittest.TestCase):
    def setUp(self):
        self.emptyList = []
        self.list1 = [1, 2, 3, 4]
        self.list1String="[1, 2, 3, 4]"
        self.list1plus1str="[2, 3, 4, 5]"
        self.stringTested="a"
        self.unsortedHello = ["l","o","\n","e","h","l"]
        self.unsortedHelloOrder = [3,5,6,2,1,4]
        self.nonAcumulatedList = [1,0,2,5,0,10]
        self.acumulatedSumList = [1,1,3,8,8,18]
        self.sortedHello = ["h","e","l","l","o","\n"]

    def test_map_and_str(self):
        stringResult = map_and_str(str, self.emptyList)
        self.assertEqual(stringResult, "[]")
        stringResult = map_and_str(str, self.emptyList, '(', ')')
        self.assertEqual(stringResult, "()")
        stringResult = map_and_str(str, self.emptyList, '(', ']')
        self.assertEqual(stringResult, "(]")
        stringResult = map_and_str(str, self.list1)
        self.assertEqual(stringResult, self.list1String)
        stringResult = map_and_str(lambda x: str(x+1), self.list1)
        self.assertEqual(stringResult, self.list1plus1str)

    def test_sort_using_2nd_list(self):
        a = self.unsortedHello
        b = self.unsortedHelloOrder
        a1,b1 = sort_using_2nd_list(a, b)
        self.assertEqual(a1, self.sortedHello)
        self.assertEqual(b1, list(range(1,7)))
    
    def test_get_best(self):
        a = self.unsortedHello
        b = self.unsortedHelloOrder
        maxA = get_best(a, b)
        self.assertEqual(maxA, "\n")
        
    def test_accumulate(self):
        a = self.nonAcumulatedList
        b = accumulate_sums(a)
        self.assertEqual(b, self.acumulatedSumList)
        
if __name__=='__main__':
    unittest.main()
