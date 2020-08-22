from itertools import repeat
from .BaseTypes import Container, LimitedValue
from .Utility import function_to_str

class Genotype(Container):
    def __init__(self, elements):
        super().__init__(elements)

    def __repr__(self):
        return 'Genotype({})'.format(repr(self.elements))
      
    def __str__(self):
        return '{}'.format(str(self.elements))
        
class Representation(Container):
    def __init__(self, genotype, fenotypeFun, Class):
        self._Class = Class

        for element in genotype:
            if not isinstance(element, self._Class):
                raise TypeError(("{} needs an iterable of {}(s) to be built "+
                                "but a {} was passed"). \
                                format(type(self).__name__,
                                       self._Class.__name__,
                                       type(element)))
        super().__init__(genotype)
        self.fenotypeFun = fenotypeFun

    @property
    def genotype(self):
        return Genotype(self.elements)

    def fenotype(self):
        return self.fenotypeFun(self.genotype)

    def append(self, elements):
        return type(self)(self.elements.append(elements), self.fenotypeFun)

    def setitem(self, key, value):
        return type(self)(self.elements.setitem(key, value), self.fenotypeFun)

    def __getitem__(self, key):
        if type(key) == slice:
            return type(self)(self.elements[key], self.fenotypeFun)
        else:
            return super().__getitem__(key)
    
    def __eq__(self, other):
        return (self.fenotype()==other.fenotype() and \
                self.genotype==other.genotype)

    def __str__(self):
        return str(self.fenotype())

    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__,
                                   repr(self.elements),
                                   self.fenotypeFun.__name__)
        
class Nucleotide(LimitedValue):
    def __init__(self, value=None, domain=None):
            super().__init__(value, domain)
    
    def issametype(self, other):
        return self.domain==other.domain

    def __eq__(self, other):
        return self.value==other.value and self.domain==other.domain
        
    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return 'Nucleotide({}, {})'.format(repr(self.value),
                                           repr(self.domain))

class Gene(Representation):
    def __init__(self, nucleotides, fenotypeFun):
        super().__init__(nucleotides, fenotypeFun, Nucleotide)
    
    @property
    def nucleotides(self):
        return self.genotype

class Chromosome(Representation):
    def __init__(self, genes, fenotypeFun):
        super().__init__(genes, fenotypeFun, Gene)
        
    @property
    def genes(self):
        return self.genotype

class Individual(Representation):
    def __init__(self, chromosomes, fenotypeFun):
        super().__init__(chromosomes, fenotypeFun, Chromosome)
        
    @property
    def chromosomes(self):
        return self.genotype

class Population(Container):
    def __init__(self, individuals=list()):
        for indiv in individuals:
            if not isinstance(indiv, Individual):
                raise TypeError(
                    "Population needs an iterable of Individual(s) to be built"+
                    ", but a {} was passed".format(type(indiv)))
        super().__init__(individuals)
        
    @property
    def individuals(self):
        return self.elements
                
    def __str__(self):
        return '\n'.join(str(indiv) for indiv in self)

    def __repr__(self):
        return '{}({})'.format(type(self).__name__,
                               ',\n'.join(repr(indiv) for indiv in self))

class Fitness_function(object):
    def __init__(self, system_simulation, evaluate_solution):
        self.system_simulation = system_simulation
        self.evaluate_solution = evaluate_solution

    def calc_fitness(self, individual):
        fenotype = individual.fenotype()
        simulationResult = self.system_simulation(fenotype)
        fitness = self.evaluate_solution(simulationResult)
        return fitness

    def __call__(self, population):
        fitnessList = [self.calc_fitness(indiv) for indiv in population]
        return fitnessList

    def __str__(self):
        return ('\n# system_simulation:\n'+
                '{}\n'+
                '# evaluate_solution:\n'+
                '{}').format(function_to_str(self.system_simulation), 
                             function_to_str(self.evaluate_solution))

    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__,
                                   self.system_simulation.__name__,
                                   self.evaluate_solution.__name__)

class Selection_function(object):
    def __init__(self, process_fitness, select_individuals):
        self.process_fitness = process_fitness
        self.select_individuals = select_individuals

    def __call__(self, population, fitnessList):
        selectionParameters = self.process_fitness(fitnessList)
        newPopulation = self.select_individuals(population, selectionParameters)
        return newPopulation

    def __str__(self):
        return ('\n# process_fitness:\n'+
               '{}\n'+
               '# select_individuals:\n'+
               '{}').format(function_to_str(self.process_fitness),
                            function_to_str(self.select_individuals))

    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__,
                                   self.system_simulation.__name__,
                                   self.evaluate_solution.__name__)

class Crossover_function(object):
    def __init__(self, choose_parents, recombine_parents, desiredSize):
        self.choose_parents = choose_parents
        self.recombine_parents = recombine_parents
        self.desiredSize = desiredSize

    def __call__(self, population, fitnessList=None):
        newPopulation = Population()
        while len(newPopulation) < self.desiredSize:
            parents = self.choose_parents(population, fitnessList)
            children = self.recombine_parents(parents)
            newPopulation = newPopulation.append(children)
        return newPopulation

    def __str__(self):
        return ('\n# choose_parents:\n'+
                '{}\n'+
                '# recombine_parents:\n'+
                '{}\n'+
                'desiredSize = {}'
                ).format(function_to_str(self.choose_parents), 
                         function_to_str(self.recombine_parents),
                         self.desiredSize)

    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.choose_parents.__name__,
                                       self.recombine_parents.__name__,
                                       self.desiredSize)

class Mutation_function(object):
    def __init__(self, willmutate, choose_nucleotides, f_transform):
        self.willmutate = willmutate
        self.choose_nucleotides = choose_nucleotides
        self.f_transform = f_transform

    def __call__(self, population, fitnessList=repeat(None)):
        newPopulation = Population()
        for individual, fitness in zip(population, fitnessList):
            if self.willmutate(individual, fitness):
                nucleotidesPositions = self.choose_nucleotides(individual, 
                                                               fitness)
                for position in nucleotidesPositions:
                    chromosome, gene, nucleotide = position
                    originalNucleotide = individual[chromosome][gene][nucleotide]
                    mutatedNucleotide = self.f_transform(originalNucleotide, 
                                                         position)
                    individual = individual.setitem(position, mutatedNucleotide)
            newPopulation = newPopulation.insert_at_end(individual)
        return newPopulation

    def __str__(self):
        return ('\n# willmutate:\n'+
                '{}\n'+
                '# choose_nucleotides:\n'+
                '{}\n'+
                '# f_transform:\n'+
                '{}').format(function_to_str(self.willmutate), 
                             function_to_str(self.choose_nucleotides),
                             function_to_str(self.f_transform))

    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.willmutate.__name__,
                                       self.choose_nucleotides.__name__,
                                       self.f_transform.__name__)

class End_function(object):
    def __init__(self, maxGeneration, other_condition=None):
        self.maxGeneration = maxGeneration
        self.other_condition = other_condition

    def __call__(self, population, fitnessList, generation):
        if generation > self.maxGeneration:
            return True
        elif self.other_condition==None:
            return False
        else:
            return self.other_condition(population, fitnessList, generation)

    def __str__(self):
        return ('\nmaxGeneration = {}\n'+
                'other_condition = {}'
                ).format(self.maxGeneration,
                         function_to_str(self.other_condition))

    def __repr__(self):
        if self.other_condition==None:
            return '{}({})'.format(type(self).__name__,
                                   self.maxGeneration)
        else:
            return '{}({}, {})'.format(type(self).__name__,
                                       self.maxGeneration,
                                       self.other_condition.__name__)
