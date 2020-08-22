import unittest
import sys
import importlib
import BaseTypes
import model

class TestNucleotide(unittest.TestCase):
    def setUp(self):
        self.domain1 = BaseTypes.IntInterval(0,10)
        self.domain2 = BaseTypes.CharSet('neatural')
        self.nucleo1 = model.Nucleotide(5, self.domain1)
        self.nucleo2 = model.Nucleotide('t', self.domain2)

    def test_get_domain(self):
        self.assertEqual(self.nucleo1.domain, self.domain1)
        self.assertEqual(self.nucleo2.domain, self.domain2)

    def test_get_value(self):
        self.assertEqual(self.nucleo1.value, 5)
        self.assertEqual(self.nucleo2.value, 't')
        
    def test_issametype(self):
        nucleo2 = model.Nucleotide(domain=BaseTypes.IntInterval(0,10))
        nucleo3 = model.Nucleotide(domain=BaseTypes.IntInterval(0,9))
        nucleo4 = model.Nucleotide(domain=BaseTypes.IntInterval(1,10))
        nucleo5 = model.Nucleotide(domain=BaseTypes.FloatInterval(0,10))
        nucleo6 = model.Nucleotide(domain=BaseTypes.CharSet('neatural'))
        nucleo7 = model.Nucleotide(domain=BaseTypes.CharSet('larutean'))

        self.assertTrue(self.nucleo1.issametype(nucleo2))
        self.assertFalse(self.nucleo1.issametype(nucleo3))
        self.assertFalse(self.nucleo1.issametype(nucleo4))
        self.assertFalse(self.nucleo1.issametype(nucleo5))
        self.assertTrue(nucleo6.issametype(nucleo7))
        
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
        
    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestNucleotide)
    unittest.TextTestRunner().run(loader)
