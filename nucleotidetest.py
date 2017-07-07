from ga import Nucleotide
from GTypes import *
from GDefaults import *
from gaDefaults import *

testData = GInt(6)

def creation_test():
    nucleo = Nucleotide(testData)
    assert(nucleo.data==testData)
    assert(nucleo.data is not testData)
    
def default_creation_test():
    nucleo = Nucleotide()
    assert(nucleo.data==DEFAULT_DATA)
    
def copy_test():
    nucleo = Nucleotide(testData)
    nucleoCopy = nucleo.copy()
    assert(nucleo==nucleoCopy)
    assert(nucleo is not nucleoCopy)
    
def new_value_test():
    nucleo=Nucleotide(testData)
    nucleo.data = 10
    assert(nucleo.data.isinsameinterval(testData))
    assert(nucleo.data!=testData)
    
def new_type_test():
    nucleo=Nucleotide(testData)
    nucleo.data = GReal(10.5)
    assert(type(nucleo.data)!=type(testData))

def new_random_value_test():
    nucleo = Nucleotide(testData)
    nucleo.new_random_value()
    assert(nucleo.data!=testData)
    
def issametype_test():
    nucleo1=Nucleotide(GInt(5,1,10))
    nucleo2=Nucleotide(GInt(7,1,10))
    nucleo3=Nucleotide(GInt(1,1,5))
    assert(nucleo1.issametype(nucleo2)==True)
    assert(nucleo1.issametype(nucleo3)==False)