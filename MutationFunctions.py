from .model import Mutation_function, Nucleotide
from random import random, choice

# ----------------------- willmutate factories -----------------------
class Random_willmutate():
    def __init__(self, mutationProbability):
        self.mutationProbability = mutationProbability
    
    def __call__(self, individual, fitness=None):
        if random()<self.mutationProbability:
            return True
        else:
            return False
# ----------------------- willmutate functions -----------------------
always_mutate = Random_willmutate(1)
never_mutate = Random_willmutate(0)
# ------------------- choose_nucleotides factories -------------------
class Nucleotide_random_choice():
    def __init__(self, numberNucleotides):
        self.numberNucleotides = numberNucleotides
    
    def __call__(self, individual, fitness=None):
        positions = list()
        while len(positions)<self.numberNucleotides:
            chromosome = choice(range(len(individual)))
            gene = choice(range(len(individual[chromosome])))
            nucleotide = choice(range(len(individual[chromosome][gene])))
            position = (chromosome, gene, nucleotide)
            if position not in positions:
                positions.append(position)
        return positions
# ------------------- choose_nucleotides functions -------------------
one_random_nucleotide = Nucleotide_random_choice(1)
# ----------------------- f_transform functions ----------------------
def random_value_transform(nucleotide, position=None):
    return Nucleotide(nucleotide.get_random_value(), nucleotide.domain)
# ------------------- mutation_function factories --------------------
def make_single_mutation(mutationProbability):
    return Mutation_function(Random_willmutate(mutationProbability),
                             one_random_nucleotide,
                             random_value_transform)
