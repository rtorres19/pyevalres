import unittest
from BaseTypes import CharSet, IntInterval, FloatInterval, Set, LimitedValue
from Defaults import DEFAULT_CHAR_SET
from string import ascii_uppercase

class LimitedValueTest(unittest.TestCase):
    def setUp(self):
        self.intervalMin = 0
        self.intervalMax = 100
        self.setList = ['A','G','T','C']
        self.limited_0_100 = LimitedValue(2, IntInterval(self.intervalMin,
                                                         self.intervalMax))
        self.limitedNaturalSet = LimitedValue('A', Set(self.setList))

    def test_get_min(self):
        self.assertEqual(self.limited_0_100.min, self.intervalMin)
    def test_get_max(self):
        self.assertEqual(self.limited_0_100.max, self.intervalMax)

    def test_get_set(self):
        self.assertEqual(self.limitedNaturalSet.set, set(self.setList))
        
    def test_isindomain(self):
        self.assertTrue(self.limited_0_100.isindomain(0))
        self.assertTrue(self.limited_0_100.isindomain(100))
        self.assertTrue(self.limited_0_100.isindomain(50))
        self.assertFalse(self.limited_0_100.isindomain(101))

        self.assertTrue(self.limitedNaturalSet.isindomain('T'))
        self.assertFalse(self.limitedNaturalSet.isindomain('F'))
        
    def test_copy(self):
        copy1 = self.limited_0_100.copy()
        self.assertEqual(copy1.value, self.limited_0_100.value)
        self.assertEqual(copy1.domain, self.limited_0_100.domain)
        self.assertIsNot(copy1, self.limited_0_100)

    def test_get_random_value(self):
        for i in range(1000):
            randomValue = self.limited_0_100.get_random_value()
            self.assertTrue(self.limited_0_100.isindomain(randomValue))

        
if __name__ == '__main__':
    unittest.main()

