import unittest
from BaseTypes import CharSet
import Defaults

class CharSetTest(unittest.TestCase):
    def setUp(self):
        self.natural = CharSet('AGTC')
        
    def test_in(self):
        self.assertTrue("A" in self.natural)
        self.assertTrue("G" in self.natural)
        self.assertFalse("H" in self.natural)

    def test_eq(self):
        auxSet = CharSet(["A", "G", "T", "C"])
        self.assertTrue(auxSet == self.natural)
        self.assertTrue(self.natural == 'AGTC')

    def test_random_value(self):
        for i in range(1000):
            self.assertIn(self.natural.get_random_value(), self.natural)

if __name__ == '__main__':
    unittest.main()
