import ga
import random
import Utility
    
if __name__=="__main__":
    
    def gauss_distrib(mu, sigma):
        return random.gauss(mu, sigma)
    
    
    def count_number(numbers, n):
        counter = 1
        for number in numbers:
            if number==n:
                counter+=1
        return counter
    
    @ga.generic_fitness
    def count_zeros(individual):
        numbers = individual.fenotype()[0]
        sum = 0
        for number in numbers:
            sum+=number
        counter = count_number(numbers, 10)
        fitness = counter-abs((100-sum)/(100*10))
        return fitness
        
    def max_gen(max):
        def max_gen_f(population, generation):
            if generation>=max:
                return True
            return False
        return max_gen_f
    
    def save_fun(selectedPopulation, crossedPopulation, mutatedPopulation,
                            population, fitnessList, generation):
        if generation%10==0:
            return( "Generation: ", generation,
                    "Best individual: ", str(Utility.get_best(population,fitnessList)),
                    "Max fitness: ", max(fitnessList))
        else:
            return None
    
    popSize = 50
    mutP = 0.4
    crossP = .3
    tourney_size = 10
    maxGen = 100
    
    baseNucleotide = ga.Nucleotide()
    gene = ga.Gene([baseNucleotide], lambda x: x[0].data.value)
    chromosome = ga.Chromosome([gene for i in range(10)])
    individual = ga.Individual([chromosome])
    
    pop= ga.Population.random([individual for i in range(popSize)])
    
    inipop=pop
    print("\nInitial population:")
    
    for indiv in inipop:
        print(indiv)
    
    (finpop, fitnessList, resultsper10)=ga.genetic_algorithm(population=pop,
                                                    fitness_fun=count_zeros,
                                                    selection_fun=ga.tournament(tourney_size),
                                                    crossover_fun=ga.single_point(crossP),
                                                    mutation_fun=ga.simple_mutation(mutP),
                                                    end_fun=max_gen(maxGen),
                                                    save_fun=save_fun)
    
    print("\nFinal population: ")
    for indiv in finpop:
        print(indiv)
    print("\nBest individual: ", Utility.get_best(finpop,fitnessList), "Max fitness: ", max(fitnessList),"\n\n\n")
    for result in resultsper10:
        print (result,"\n")