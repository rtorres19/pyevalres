import unittest
import sys
import importlib
from BaseTypes import IntInterval, CharSet
import model

class TestPopulation(unittest.TestCase):
    def setUp(self):
        self.rowN = model.Nucleotide(domain=IntInterval(1,9))
        self.columnN = model.Nucleotide(domain=CharSet('abcdefgh'))
        self.positionG = model.Gene((self.rowN,self.columnN),
                                    lambda nucleos: \
                                    (str(nucleos[0].value) + 
                                     str(nucleos[1].value)))
        self.fenotype1 = lambda genotype: model.Container(gene.fenotype() \
                                                          for gene in genotype)
        self.fenotype2 = lambda genotype: model.Container(chromo.fenotype() \
                                                          for chromo in genotype)
        self.onePositionC = model.Chromosome([self.positionG], self.fenotype1)
        self.eightQueens = model.Individual([self.onePositionC \
                                             for i in range(8)],
                                            self.fenotype2)
        self.population = model.Population([self.eightQueens \
                                            for i in range(10)])
        
    def test_get_individuals(self):
        individuals = self.population.individuals
        [self.assertEqual(indiv,self.eightQueens) for indiv in individuals]

    def test_make_void_population(self):
        population = model.Population()
        self.assertTrue(True)
        
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

    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestPopulation)
    unittest.TextTestRunner().run(loader)

