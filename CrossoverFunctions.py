from .model import Crossover_function
from random import sample, randint, random

# --------------------- choose_parents factories ---------------------
class Parent_random_choice():
    def __init__(self, numberParents):
        self.numberParents = numberParents
    
    def __call__(self, population, fitnessList=None):
        return sample(list(population), self.numberParents)

# --------------------- choose_parents functions ---------------------
two_random_parents = Parent_random_choice(2)
# -------------------- recombine_parents factories -------------------

# class Single_point_recombination():
#     def __init__(self, position=None):
#         self.position = position

#     def __call__(self, parents):
#         father, mother = parents
#         if self.position==None:
#             j = randint(0, min(len(father), len(mother)))
#         else:
#             j = self.position
#         child1 = father[:j].append(mother[j:])
#         child2 = mother[:j].append(father[j:])
#         return (child1, child2)

class Multi_point_recombination():
    def __init__(self, crossProb=1, numberOfPoints=None, positions=None):
        self.crossProb = crossProb
        if numberOfPoints==None and positions!=None:
            self.numberOfPoints = len(positions)
        else:
            self.numberOfPoints = numberOfPoints
        self.positions = positions                

    def __call__(self, parents):
        father, mother = parents
        if random()>=self.crossProb:
            return (father, mother)
        # random number of points
        if self.numberOfPoints==None:
            numberOfPoints = randint(1, min(len(father),len(mother)))
        # fixed number of points
        else:
            numberOfPoints = self.numberOfPoints
        # random positions (once number of points has been established)
        if self.positions==None:
            positions = sorted(sample(range(1, min(len(father),len(mother))),
                                      numberOfPoints))
        # fixed positions
        else:
            # some positions are random and some fixed
            if numberOfPoints>len(self.positions):
                diff = numberOfPoints - len(positions)
                randomPositions = list()
                while len(randomPositions)<diff:
                    num = randint(1, min(len(father),len(mother)))
                    if num not in positions:
                        randomPositions.append(num)
                positions = sorted(self.positions + randomPositions)
            # choose numberOfPoints from the positions
            elif numberOfPoints<len(self.positions):
                positions = sorted(sample(self.positions, number_of_points))
            else:
                positions = self.positions
        
        child1 = father
        child2 = mother
        for i in range((numberOfPoints+1)//2):
            start = positions[2*i]
            try:
                end = positions[2*i+1]
            except IndexError:
                child1 = child1[:start].append(mother[start:])
                child2 = child2[:start].append(father[start:])
                return (child1, child2)
            child1 = child1.setslice(start, end, mother[start:end])
            child2 = child2.setslice(start, end, father[start:end])
        return (child1, child2)

def make_single_point_recombination(crossProb, position=None):
    return Multi_point_recombination(crossProb, 1, position)

def make_two_point_recombination(crossProb, positions=None):
    return Multi_point_recombination(crossProb, 2, positions)

def make_full_recombination(crossProb):
    return Multi_point_recombination(crossProb)
# ------------------- crossover_function factories -------------------
def make_single_point_crossover(desiredSize, crossProb=1):
    return Crossover_function(two_random_parents,
                              make_single_point_recombination(crossProb),
                              desiredSize)

def make_full_crossover(desiredSize, crossProb=1):
    return Crossover_functions(two_random_parents,
                               make_full_recombination(crossProb),
                               desiredSize)
