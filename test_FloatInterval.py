import unittest
from BaseTypes import FloatInterval

class FloatIntervalTest(unittest.TestCase):
    def setUp(self):
        self.limit_1_5 = FloatInterval(1.0, 5.0)

    def test_wrong_limits(self):
        with self.assertRaises(TypeError):
            FloatInterval(4.0, 3.0)
        with self.assertRaises(TypeError):
            FloatInterval(3.0, 3.0)

    def test_in(self):
        self.assertTrue(3.0 in self.limit_1_5)
        self.assertTrue(2 in self.limit_1_5)
        self.assertFalse(8.0 in self.limit_1_5)

    def test_eq(self):
        auxInterval = FloatInterval(1.0, 5.0)
        self.assertTrue(auxInterval == self.limit_1_5)

    def test_random_value(self):
        for i in range(1000):
            self.assertIn(self.limit_1_5.get_random_value(), self.limit_1_5)

if __name__ == '__main__':
    unittest.main()
