import string
import model
import BaseTypes

DEFAULT_INT_MIN = 0
DEFAULT_INT_MAX = 10
DEFAULT_INT_INTERVAL = BaseTypes.IntInterval(DEFAULT_INT_MIN, DEFAULT_INT_MAX)

DEFAULT_FLOAT_MIN = 0.0
DEFAULT_FLOAT_MAX = 10.0
DEFAULT_FLOAT_INTERVAL = BaseTypes.FloatInterval(DEFAULT_FLOAT_MIN, 
                                                 DEFAULT_FLOAT_MAX)

DEFAULT_CHAR_SET = string.ascii_lowercase

def default_fenotypeFun(genotype):
    return model.Container(elem.fenotype() for elem in genotype)

def default_gene_fenotypeFun(nucleotides):
    return nucleotides[0].value
