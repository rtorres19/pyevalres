from Utility import *
from GDefaults import *
from gaDefaults import *
from GTypes import *
from GRandom import *
from functools import wraps
import random

class Nucleotide(object):
    """ The computer representation of the genes
        
        Attr:
            data: The data of the neuclotide
        
        Methods:
            copy(): Creates a new nucleotide with the same data
        
    """
    def __init__(self, data=DEFAULT_DATA):
        self._data = data.copy()
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, newValue):
        # If newValue is a GType, set it as it is
        if(isinstance(newValue, GType)):
            self._data = newValue.copy()
        # otherwise, set it to the data's value
        else:
            self._data.value = newValue
    
    def copy(self):
        return Nucleotide(self.data)
    
    def new_random_value(self):
        self.data.new_random_value()
    
    def ga_repr(self):
        return repr(self.data)
    
    def ga_prepr(self):
        return str(self.data)
        
    def __eq__(self, x):
        return self.data==x.data
    
    def issametype(self, x):
        return self.data.isinsameinterval(x.data)
        
    def __str__(self):
        return str(self.data)
    
class Gene(GContainer):
    """ A group of nucleotides that completely represent a single characteristic of
        an individual
        
        Attr:
            nucleotides: A list with the nucleotides of the gene
            fenotype_fun: A function that combines the nucleotides into information
                fenotype_fun(nucleotides) -> object
            
        Methods:
            fenotype() -> fenotype_fun(self.nucleotides)
    """
    
    def __init__(self, nucleotides, fenotype_fun=DEFAULT_FENOTYPE_FUN):
        """ Create a Gene from a list of nucleotides
            
            Uses:
                Gene(list_of_nucleotides, fenotype_function): create a gene from a
                    list of nucleotides
                Gene(list_of_nucleotides): create a gene with a default fenotype_function
        """
        self.fenotype_fun = fenotype_fun
        self.nucleotides = nucleotides
        
    @property
    def nucleotides(self):
        return self.elements
    @nucleotides.setter
    def nucleotides(self, nucleotides):
        self.elements = [nucleotide.copy() for nucleotide in nucleotides]
    
    def fenotype(self):
        """ Returns the fenotype of the gene
        """
        return self.fenotype_fun(self.nucleotides)
    
    def copy(self):
        return Gene(self.nucleotides, self.fenotype_fun)
    
    def __str__(self):
        return str(self.fenotype())
        
    def __eq__(self, gene):
        return (gene.fenotype_fun==self.fenotype_fun and gene.nucleotides==self.nucleotides)
    
    @staticmethod
    def random(nucleotides, fenotype_fun):
        newGene = Gene(nucleotides, fenotype_fun)
        for nucleotide in newGene:
            nucleotide.new_random_value()
            
        return newGene
    
class Chromosome(GContainer):
    """ A group of genes contained together for easiness in crossover
    
        Attr:
            genes: A list with all the genes of the chromosome
            
        Methods:
            fenotype() -> [genes[0].fenotype(), genes[1].fenotype(), ...]
    """
    
    def __init__(self, genes):
        """ Initialize a chromosome from the genes list provided, or from 
            another Chromosome
        
            Uses:
                Chromosome(genes): Create a Chromosome from a list of genes
            
        """
        self.elements = [Gene(gene.nucleotides, gene.fenotype_fun) for gene in genes]
        
    @property
    def genes(self):
        return self.elements
    @genes.setter
    def genes(self, genes):
        self.elements = [gene.copy() for gene in genes]
    
    def fenotype(self):
        fenotypes = [gene.fenotype() for gene in self]
        return fenotypes
    
    def copy(self):
        return Chromosome(self.genes)
    
    def __str__(self):
        return str(self.fenotype())
        
    def __eq__(self, chromosome):
        return (self.genes==chromosome.genes)
        
    @staticmethod
    def random(genes):
        newGenes = [Gene.random(gene.nucleotides, gene.fenotype_fun) for gene in genes]
        return Chromosome(newGenes)
        
class Individual(GContainer):
    """ A group of chromosomes contained together that describe a complete
        solution
    
        Attr:
            chromosomes: A list with all the chromosomes of the individual
            
        Methods:
            fenotype() -> [chromo[0].fenotype(), chromo[1].fenotype(), ...)
    """
    def __init__(self, chromosomes):
        """ Initialize an individual from the chromosomes list provided or from
            another individual
            
            Uses:
                Individual(chromosomes): Create an Individual from a list of chromos
            
        """
        self.elements = [Chromosome(chromosome.genes) for chromosome in chromosomes]
                    
    @property
    def chromosomes(self):
        return self.elements
    @chromosomes.setter
    def chromosomes(self, chromosomes):
        self.elements = [chromosome.copy() for chromosome in chromosomes]
        
    def copy(self):
        return Individual(self.chromosomes)
    
    def fenotype(self):
        fenotypes = [chromosome.fenotype() for chromosome in self]
        return fenotypes
    
    def __str__(self):
        return str(self.fenotype())
    
    @staticmethod
    def random(chromosomes):
        newChromosomes = [Chromosome.random(chromosome.genes) for chromosome in chromosomes]
        return Individual(newChromosomes)
    
class Population(GContainer):
    """ A group of individuals
        
        Attr:
            individuals: A list with all the individuals of the population
            
        Methods:
        
    """
    def __init__(self, individuals=list()):
        """ Create a population from a list of individuals.
            Defaults to an empty population
            
            Args:
                individuals: the list of individuals that will be in the population
        """
        self.individuals = individuals
        
    @property
    def individuals(self):
        return self.elements
    @individuals.setter
    def individuals(self, individuals):
        self.elements = [individual.copy() for individual in individuals]
    
    def copy(self):
        return Population(self.individuals)
        
    @staticmethod
    def random(individuals):
        newIndividuals = [Individual.random(individual.chromosomes) for individual in individuals]
        return Population(newIndividuals)
    
    def __str__(self):
        retStr=''
        for indiv in self:
            retStr+="\n"
            retStr+= str(indiv)
        return retStr
    
def genetic_algorithm(population, fitness_fun, selection_fun,
                      crossover_fun, mutation_fun, end_fun, save_fun):
    """ Simple genetic algorithm
            
        Returns:
            The best individual of the last generation and the data saved from the save function
    """
    generation = 0
    saved_data = []
    fitnessList = fitness_fun(population)
    
    while end_fun(population, generation)==False:
        
        bestIndividual = get_best(population, fitnessList).copy()
        bestFitness = max(fitnessList)
        
        selectedPopulation = selection_fun(population, fitnessList)
        
        crossedPopulation = crossover_fun(selectedPopulation)
        
        mutatedPopulation = mutation_fun(crossedPopulation)
        
        population = mutatedPopulation.copy()
        
        fitnessList = fitness_fun(population)
        
        merge_sort_and_unpack_using_2nd_list(population, fitnessList)
        
        population[0] = bestIndividual.copy()
        fitnessList[0] = bestFitness
        
        new_data = save_fun(selectedPopulation, crossedPopulation, mutatedPopulation,
                            population, fitnessList, generation)
        if new_data!=None:
            saved_data.append(new_data)
        
        generation += 1
        
    return (population, fitnessList, saved_data)
    
def generic_fitness(individual_fitness):
    
    @wraps(individual_fitness)
    def wrapper(population, min=False):
        if min==False:
            fitnessList = [individual_fitness(individual) for individual in population]
        else:
            fitnessList = [-1*individual_fitness(individual) for individual in population]
        return fitnessList
        
    return wrapper
    
def generic_crossover(crossover_over_pairs):
    
    @wraps(crossover_over_pairs)
    def wrapper(population):
        newPopulation = Population()
        numCross = (len(population) // 2)
        for i in range(numCross):
            parent1 = population[2*i]
            parent2 = population[2*i + 1]
            (offspring1, offspring2) = crossover_over_pairs(parent1, parent2)
            newPopulation.append(offspring1)
            newPopulation.append(offspring2)
        if len(newPopulation)<len(population):
            newPopulation.append(population[-1].copy())
        return newPopulation
        
    return wrapper
    
def generic_selection(select_an_individual):
    
    @wraps(select_an_individual)
    def wrapper(population, fitnessList):
        positiveFitness = add_offset_for_positive_values(fitnessList)
        normalFitness = normalize(positiveFitness)
        probabilities = normalFitness
        
        newPopulation = Population()
        bestIndividual = get_best(population, fitnessList)
        newPopulation.append(bestIndividual.copy())
        
        while len(newPopulation)<len(population):
            selectedIndi = select_an_individual(population, probabilities)
            newPopulation.append(selectedIndi)
        return newPopulation
        
    return wrapper
    
def generic_mutation(individual_mutation):

    @wraps(individual_mutation)
    def wrapper(population):
        newPopulation = population.copy()
        for individual in newPopulation:
            individual_mutation(individual)
        return newPopulation
        
    return wrapper
    
DEFAULT_MAX_FITNESS = 1000000

@generic_selection
def roulette_wheel(population, probL):
    # Make a list of the acumulated probabilities
    acum = 0
    acumProb = list()
    for p in probL:
        acum+= p
        acumProb.append(acum)
    # Generate a random number in [0,1)
    r=random.random()
    # Return the randomly chosen individual
    for i in range(len(acumProb)):
        if i==0:
            preProb=0
        else:
            preProb=acumProb[i-1]
        if preProb <= r < acumProb[i]:
            return population[i].copy()

def tournament(tourney_size):
    
    @generic_selection
    def tourney(population, probL):
        mergedPopAndProb = list(zip(population, probL))
        auxPop = Population()
        auxProb = list()
        for i in range(tourney_size):
            auxIndiAndProb = random.choice(mergedPopAndProb)
            auxPop.append(auxIndiAndProb[0].copy())
            auxProb.append(auxIndiAndProb[1])
        return get_best(auxPop, auxProb).copy()

    return tourney

def single_gen(crossP):
    @generic_crossover
    def single_gen_cross(father, mother):
        r=random.random()
        if r > crossP:
            return father, mother
            
        thisChrom = random.choice(range(len(father)))
        fatherChrom= father[thisChrom]
        motherChrom= mother[thisChrom]
        
        thisGene = random.choice(range(len(fatherChrom)))
        fatherGene = fatherChrom[thisGene]
        motherGene = motherChrom[thisGene]
        
        offspr1 = father.copy()
        offspr2 = mother.copy()
        
        offspr1[thisChrom][thisGene]=motherGene.copy()
        offspr2[thisChrom][thisGene]=fatherGene.copy()
        
        return offspr1,offspr2
        
    return single_gen_cross

def single_point(crossP):
    @generic_crossover
    def single_p(father, mother):
        r = random.random()
        if r>crossP:
            return father, mother
        
        offspr1 = father.copy()
        offspr2 = mother.copy()
        
        thisChrom = random.choice(range(len(father)))
        fatherChrom= father[thisChrom]
        
        iniGene= random.choice(range(len(fatherChrom)))
        
        newGenesFa= [ father[thisChrom][i].copy() for i in range(iniGene,len(fatherChrom))]
        newGenesMo= [ mother[thisChrom][i].copy() for i in range(iniGene,len(fatherChrom))]
        
        offspr1[thisChrom][iniGene:] = newGenesMo
        offspr2[thisChrom][iniGene:] = newGenesFa
        
        return offspr1, offspr2
        
    return single_p

def simple_mutation(mutP):
    @generic_mutation
    def simple_mut(individual):

        def mutate_nucleo(individual):
            thisChrom = random.choice(range(len(individual)))
            choicedChrom= individual[thisChrom]
            
            thisGene = random.choice(range(len(choicedChrom)))
            choicedGene= choicedChrom[thisGene]
            
            thisNucleo= random.choice(range(len(choicedGene)))
            choicedNucleo= choicedGene[thisNucleo]
            choicedNucleo.new_random_value()
            
        r=random.random()
        if r<=mutP:
            mutate_nucleo(individual)
    return simple_mut