import unittest
from model import Genotype

class TestGenotype(unittest.TestCase):
    def setUp(self):
        self.elements = (1,1,2,2,3,3)
        self.geno1 = Genotype(self.elements)

    def test_get_elements(self):
        self.assertEqual(self.geno1.elements, self.elements)

    def test_get_element(self):
        for i in range(len(self.elements)):
            self.assertEqual(self.geno1[i], self.elements[i])

    def test_copy(self):
        genoCopy = self.geno1.copy()
        self.assertEqual(self.geno1, genoCopy)
        self.assertIsNot(self.geno1, genoCopy)

if __name__=='__main__':
    unittest.main()

