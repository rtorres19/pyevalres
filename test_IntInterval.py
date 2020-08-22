import unittest
from BaseTypes import IntInterval

class IntIntervalTest(unittest.TestCase):
    def setUp(self):
        self.limit_1_5 = IntInterval(1, 5)

    def test_wrong_limits(self):
        with self.assertRaises(TypeError):
            IntInterval(4, 3)
        with self.assertRaises(TypeError):
            IntInterval(3, 3)

    def test_in(self):
        self.assertTrue(3 in self.limit_1_5)
        self.assertFalse(8 in self.limit_1_5)
        self.assertFalse(3.4 in self.limit_1_5)

    def test_eq(self):
        auxInterval = IntInterval(1, 5)
        self.assertTrue(auxInterval == self.limit_1_5)

    def test_random_value(self):
        for i in range(1000):
            self.assertIn(self.limit_1_5.get_random_value(), self.limit_1_5)

if __name__ == '__main__':
    unittest.main()
