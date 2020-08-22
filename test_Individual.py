import unittest
import sys
import importlib
import BaseTypes
import model

class TestIndividual(unittest.TestCase):
    def setUp(self):
        self.rowN = model.Nucleotide(domain=BaseTypes.IntInterval(1,8))
        self.columnN = model.Nucleotide(domain=BaseTypes.CharSet('abcdefgh'))
        self.positionG = model.Gene((self.rowN,self.columnN), 
                                    lambda nucleos: str(nucleos[0].value)+ \
                                                    str(nucleos[1].value))
        self.onePositionC = model.Chromosome([self.positionG], 
                                             self.simple_fenotype)
        self.eightQueens = model.Individual([self.onePositionC \
                                             for i in range(8)], 
                                            self.simple_fenotype)

        
    def simple_fenotype(self,genotype):
        return tuple(elem.fenotype() for elem in genotype)
    
    def test_get_chromosomes(self):
        chromosomes = self.eightQueens.chromosomes
        map(lambda chromosome: self.assertEqual(chromosome, onePositionC),
            chromosomes)
    
    def test_get_fenotypeFun(self):
        fenotype = self.eightQueens.fenotypeFun
        self.assertIs(fenotype.__code__, self.simple_fenotype.__code__)
        
    def test_fenotype(self):
        self.assertEqual(self.eightQueens.fenotype(), 
                         self.simple_fenotype(self.eightQueens.chromosomes))
    
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
        
    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestIndividual)
    unittest.TextTestRunner().run(loader)
