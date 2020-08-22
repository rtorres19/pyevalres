from . import Utility
# EvolutionaryAlgorithms.py
def identity(x):
    return x

def do_nothing(*args, **kwargs):
    pass

class Genetic_Algorithm():
    def __init__(self,
                 fitness_function,
                 selection_function,
                 crossover_function,
                 mutation_function,
                 end_function,
                 reinsertion_function = identity,
                 extra_function = do_nothing):
        self.fitness_function = fitness_function
        self.selection_function = selection_function
        self.crossover_function = crossover_function
        self.mutation_function = mutation_function
        self.end_function = end_function
        self.reinsertion_function = reinsertion_function
        self.extra_function = extra_function

    def __call__(self, initialPopulation):
        generation = 0
        fitnessList = self.fitness_function(initialPopulation)
        population = initialPopulation
        stats = list()
        while self.end_function(population, fitnessList, generation)==False:
            selectedPop = self.selection_function(population, fitnessList)
            crossedPop = self.crossover_function(selectedPop, fitnessList)
            mutatedPop = self.mutation_function(crossedPop, fitnessList)
            population = self.reinsertion_function(mutatedPop)
            fitnessList = self.fitness_function(population)
            stats.append(self.extra_function(selectedPop,crossedPop,mutatedPop,
                                             population, 
                                             fitnessList, 
                                             generation))
            generation +=1
        return (population, fitnessList, stats)
            

