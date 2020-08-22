import unittest
import sys
import importlib

from BaseTypes import *
from model import Representation, Nucleotide, Genotype, Limited

class TestRepresentation(unittest.TestCase):
    def setUp(self):
        self.genotype1 = [1,2,3,4]
        self.rep1 = Representation(self.genotype1, lambda x: sum(x), int)

    def test_get_genotype(self):
        self.assertEqual(self.rep1.genotype, self.genotype1)
    
    def test_fenotype(self):
        self.assertEqual(self.rep1.fenotype(), sum(self.rep1.genotype))

        
if __name__=='__main__':
    try:
        file_name = sys.argv[1]
        model = importlib.import_module(file_name)
    except IndexError:
        unittest.main()
        end()
        
    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestRepresentation)
    unittest.TextTestRunner().run(loader)
