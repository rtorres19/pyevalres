from ga import Nucleotide, Gene
from GTypes import *
from GDefaults import *
from gaDefaults import *

testData = GInt()
testNucleotide = Nucleotide(testData)

def creation_test():
    gene = Gene([testNucleotide], lambda x: x[0].data)
    fun = lambda x: x[0].data
    assert(gene[0]==testNucleotide)
    assert(gene.fenotype()==gene[0].data)
    
def default_creation_test():
    gene = Gene([testNucleotide])
    assert(gene[0]==testNucleotide)
    assert(gene.fenotype()==DEFAULT_FENOTYPE_FUN(gene))
    
def copy_test():
    gene = Gene([testNucleotide])
    geneCopy = gene.copy()
    assert(gene==geneCopy)
    assert(gene is not geneCopy)
    assert(gene.nucleotides is not geneCopy.nucleotides)
    
def random_creation_test():
    gene = Gene.random([testNucleotide], DEFAULT_FENOTYPE_FUN)
    assert(gene[0]!=testNucleotide)
    assert(gene.fenotype()==DEFAULT_FENOTYPE_FUN(gene))
    