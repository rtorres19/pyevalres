import unittest
import sys
import importlib
from math import sqrt
import BaseTypes
import model

class TestChromosome(unittest.TestCase):
    def setUp(self):
        self.naturalNumberN = model.Nucleotide(domain=BaseTypes.IntInterval(0,9))
        self.lessThan100N = model.Nucleotide(domain=BaseTypes.IntInterval(0,99))
        self.distanceG = model.Gene((self.naturalNumberN, self.lessThan100N), 
                                    lambda nucleos: \
                                    nucleos[0].value + nucleos[1].value/100.0)
        self.fenotype = lambda genotype: sqrt(genotype[0].fenotype()**2 + \
                                              genotype[1].fenotype()**2)
        self.positionC = model.Chromosome((self.distanceG, self.distanceG), 
                                          self.fenotype)
        
    def test_get_genes(self):
        genes = self.positionC.genes
        map(lambda gene: self.assertEqual(gene, self.distanceG), genes)

    def test_get_fenotypeFun(self):
        fenotype = self.positionC.fenotypeFun
        self.assertEqual(fenotype, self.fenotype)
        
    def test_fenotype(self):
        self.assertEqual(self.positionC.fenotype(), 
                         self.fenotype(self.positionC.genes))    

if __name__=='__main__':
    try:
        file_name = sys.argv[1]
        model = importlib.import_module(file_name)
    except IndexError:
        unittest.main()
        end()
    except ImportError:
        if sys.argv[1].startswith('-'):
            unittest.main()
            end()
        else:
            raise
        
    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestChromosome)
    unittest.TextTestRunner().run(loader)
