import ga
import random
import Utility


def roulette_wheel_selection(population, probabilities):
    r = random.random()
    acum = 0
    for i in range(len(population)):
        acum += probabilities[i]
        if r < acum:
            return population[i].copy()
            
def all_zeros_fitness(population):
    def count_zeros(individual):
        numbers = individual.fenotype()[0]
        zero_counter = 1
        sum = 0
        for number in numbers:
            if number==0:
                zero_counter+=1
            sum+=number
        fitness = zero_counter-sum/(100*10)
        return fitness
    return ga.generic_fitness(count_zeros, population)
    
def roulette_wheel(population, fitnessL):
    
        
    return ga.generic_selection(rw_sel, population, fitnessL)

def tournament(population, fitnessL):
    def tourn_sel(population, probL):
        mergedPopAndProb = list(zip(population, probL))
        auxPop = ga.Population()
        auxProb = list()
        for i in range(tourney_size):
            auxIndiAndProb = random.choice(mergedPopAndProb)
            auxPop.append(auxIndiAndProb[0].copy())
            auxProb.append(auxIndiAndProb[1])
        return Utility.get_best(auxPop, auxProb).copy()
    return ga.generic_selection(tourn_sel, population, fitnessL)

def single_gen(population):
    def sg_cross(father, mother):
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
        
    return ga.generic_crossover(sg_cross, population)

def single_point(population):
    def sg_point(father, mother):
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
    return ga.generic_crossover(sg_point, population)

def simple_mut(population):
    
    def sp_mut(individual):
        r=random.random()
        if r<=mutP:
            mutateNucleo(individual)
            
    def mutateNucleo(individual):
        thisChrom = random.choice(range(len(individual)))
        choicedChrom= individual[thisChrom]
        
        thisGene = random.choice(range(len(choicedChrom)))
        choicedGene= choicedChrom[thisGene]
        
        thisNucleo= random.choice(range(len(choicedGene)))
        choicedNucleo= choicedGene[thisNucleo]
        choicedNucleo.new_random_value()
        
    return ga.generic_mutation(sp_mut, population)
    
def max_gen(max):
    def max_gen_f(population, generation):
        if generation>=max:
            return True
        return False
    return max_gen_f

def save_fun(selectedPopulation, crossedPopulation, mutatedPopulation,
                        population, fitnessList, generation):
    if generation%10==0:
        return ("Generation: ", generation, "Best individual: ", str(Utility.get_best(population,fitnessList)), "Max fitness: ", max(fitnessList))
    else:
        return None