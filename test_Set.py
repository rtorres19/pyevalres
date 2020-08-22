import unittest
from BaseTypes import Set

class SetTest(unittest.TestCase):
    def setUp(self):
        self.natural = Set(["A", "G", "T", "C"])

    def test_in(self):
        self.assertTrue("A" in self.natural)
        self.assertTrue("G" in self.natural)
        self.assertFalse("H" in self.natural)

    def test_eq(self):
        limitAux = Set(["A", "G", "T", "C"])
        self.assertTrue(limitAux == self.natural)

    def test_random_value(self):
        for i in range(1000):
            self.assertIn(self.natural.get_random_value(), self.natural)

if __name__ == '__main__':
    unittest.main()
