from .model import Selection_function, Population
from . import Utility
from random import sample, random
from functools import wraps

# --------------------- process_fitness functions --------------------
def identity(fitnessList):
    return fitnessList

def normalize(fitnessList):
    return Utility.normalize(fitnessList)

def rank(fitnessList):
    indexes = range(len(fitnessList))
    positions = sorted(indexes, key=lambda i: fitnessList[i])
    ranks = [0]*len(fitnessList)
    for rank, position in enumerate(positions, start=1):
        ranks[position] = rank
    return ranks

def invert(fitnessList):
    return [-1*fitness for fitness in fitnessList]

def convert_to_maximization(process_fitness):
    @wraps(process_fitness)
    def invert_and_process(fitnessList):
        convertedFitness = invert(fitnessList)
        return process_fitness(convertedFitness)
    return invert_and_process

# -------------------- select_individuals factories ---------------------
class Elitism(object):
    def __init__(self, minmax, ismin=True):
        if ismin==True:
            self.min = minmax
        else:
            self.max = minmax
    
    def __call__(self, population, parameters):
        indivParam = zip(population, parameters)
        try:
            return Population([indiv for indiv,param in indivParam \
                                         if param>=self.min])
        except AttributeError:
            return Population([indiv for indiv,param in indivParam \
                                         if param<=self.max])

def repeat_for_population_of_size(newPopSize):
    def repeat_single_indiv_selection(single_selection):
        @wraps(single_selection)
        def select_individuals(population, parameters):
            return Population([single_selection(population, parameters) \
                               for _ in range(newPopSize)])
        return select_individuals
    return repeat_single_indiv_selection

class Tournament(object):
    def __init__(self, tournamentSize, newPopSize, minimization=False):
        self.tournamentSize = tournamentSize
        self.newPopSize = newPopSize
        self.minimization = minimization
        def tournament(population, ranks):
            rankedIndivs = list(zip(population, ranks))
            rankedParticipants = sample(rankedIndivs, self.tournamentSize)
            def get_rank(rankedParticipant):
                return rankedParticipant[1]
            if self.minimization==True:
                return min(rankedParticipants, key=get_rank)[0]
            else:
                return max(rankedParticipants, key=get_rank)[0]
        self._tournaments = repeat_for_population_of_size(self.newPopSize) \
                                                         (tournament)

    def __call__(self, population, parameters):
        return self._tournaments(population, parameters)

class Roulette_wheel():
    def __init__(self, newPopSize):
        self.newPopSize = newPopSize
        def select_by_roulette(population, probabilities):
            acumProbs = Utility.accumulate_sums(probabilities)
            r = random()
            for i in range(len(acumProbs)):
                try:
                    if r>=acumProbs[i] and r<acumProbs[i+1]:
                        return population[i]
                except IndexError:
                    return population[-1]
        self._roulette = repeat_for_population_of_size(self.newPopSize) \
                                                      (select_by_roulette)

    def __call__(self, population, probabilities):
        return self._roulette(population, probabilities)

# ------------------- selection_function factories ----------------------
def make_pure_elitist_selection(process_fitness, minmax, ismin=True):
    return Selection_function(process_fitness, Elitism(minmax, ismin))

def make_rank_selection(maxRank):
    return make_pure_elitist_selection(rank, maxRank, ismin=False)

def make_min_fitness_selection(minFitness):
    return make_pure_elitist_selection(identity, minFitness, ismin=True)
    
def make_tournament_selection(tournamentSize, newPopSize, minimization=False):
    select_by_tournaments = Tournament(tournamentSize, newPopSize, minimization)
    return Selection_function(normalize, select_by_tournaments)

def make_roulette_selection(newPopSize, minimization=False):
    select_by_roulette_wheel = Roulette_wheel(newPopSize)
    if minimization==True:
        calc_probabilities = convert_to_maximization(normalize)
    else:
        calc_probabilities = normalize
    return Selection_function(calc_probabilities, select_by_roulette_wheel)
