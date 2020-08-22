import model
from BaseTypes import *
from Utility import map_and_str
import Defaults

class Nucleotide(model.Nucleotide):
    def __init__(self, value=None, domain=Defaults.DEFAULT_FLOAT_INTERVAL):
        super().__init__(value, domain)
    
    def copy(self):
        return type(self)(self.value, self.domain)
    
    def ea_repr(self):
        return repr(self.data)
    
    def ea_prepr(self):
        return str(self.data)
        
class Representation(model.Representation):
    def copy(self):
        return type(self)(self.genotype, self.fenotypeFun)
        
    def ea_repr(self):
        ea_repr_caller = lambda obj: obj.ea_repr()
        return map_and_str(ea_repr_caller, self, '(', ')')
        
    def ea_prepr(self):
        ea_prepr_caller = lambda obj: obj.ea_prepr()
        return map_and_str(ea_prepr_caller, self, '(', ')')
        
class Gene(model.Gene, Representation):
    def __init__(self, 
                 nucleotides=[Nucleotide()],
                 fenotypeFun=Defaults.default_gene_fenotypeFun):
        super().__init__(nucleotides, fenotypeFun)
        
class Chromosome(model.Chromosome, Representation):
    def __init__(self, 
                 genes=[Gene()],
                 fenotypeFun=Defaults.default_fenotypeFun):
        super().__init__(genes, fenotypeFun)

class Individual(model.Individual, Representation):
    def __init__(self,
                 chromosomes = [Chromosome()],
                 fenotypeFun = Defaults.default_fenotypeFun):
        super().__init__(chromosomes, fenotypeFun)

class Population(model.Population):
    pass

class Fitness_function(model.Fitness_function):
    pass

class Selection_function(model.Selection_function):
    pass

class Crossover_function(model.Crossover_function):
    pass

class Mutation_function(model.Mutation_function):
    pass

class End_function(model.End_function):
    pass
