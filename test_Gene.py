import unittest
import sys
import importlib
import model
import BaseTypes

class TestGene(unittest.TestCase):
    def setUp(self):
        self.naturalNumberN = model.Nucleotide(domain=BaseTypes.IntInterval(0,9))
        self.lessThan100N = model.Nucleotide(domain=BaseTypes.IntInterval(0,99))
        self.fenotype = lambda nucleos: nucleos[0].value + nucleos[1].value/10.0
        self.lessThan100G = model.Gene((self.lessThan100N, self.naturalNumberN), 
                                 self.fenotype)

    def test_get_nucleotides(self):
        nucleotides = self.lessThan100G.nucleotides
        self.assertEqual(nucleotides[0], self.lessThan100N)
        self.assertEqual(nucleotides[1], self.naturalNumberN)

    def test_get_fenotypeFun(self):
        fenotype = self.lessThan100G.fenotypeFun
        self.assertEqual(fenotype, self.fenotype)
        
    def test_fenotype(self):
        self.assertEqual(self.lessThan100G.fenotype(), 
                         self.fenotype(self.lessThan100G.nucleotides))
    
if __name__=='__main__':
    try:
        file_name = sys.argv[1]
        model = importlib.import_module(file_name)
    except IndexError:
        unittest.main()
        exit()
    except ImportError:
        if sys.argv[1].startswith('-'):
            unittest.main()
            exit()
        else:
            raise
        
    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestGene)
    unittest.TextTestRunner().run(loader)
