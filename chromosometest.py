from ga import Nucleotide, Gene, Chromosome
from GTypes import *
from GDefaults import *
from gaDefaults import *

testData = GInt()
testNucleotide = Nucleotide(testData)
fenotype_fun = lambda x: x[0].data.value
testGene = Gene([testNucleotide], fenotype_fun)

def creation_test():
    chromosome = Chromosome([testGene])
    assert(chromosome[0]==testGene)
    
def copy_test():
    chromosome = Chromosome([testGene])
    chromosomeCopy = chromosome.copy()
    assert(chromosome==chromosomeCopy)
    assert(chromosome is not chromosomeCopy)
    assert(chromosome.genes is not chromosomeCopy.genes)
    
def random_creation_test():
    chromosome = Chromosome.random([testGene])
    print(chromosome, testGene)
    assert(chromosome[0]!=testGene)