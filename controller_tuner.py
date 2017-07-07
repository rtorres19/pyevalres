import ga
import GTypes

import dynSy
import ctrl

system = dynSy.tf(num, denom)
controller = ctrl.PID()

@ga.generic_fitness
def less_control_effort_and_short_settling_time(individual):
    controller.params = individual.fenotype_fun()[0]
    closedLoopSystem = dynSy.close_loop(dynSy.join(system, controller))
    
    simulation = dynSy.simulate(closedLoopSystem)
    
    if not dynSy.isstable(simulation):
        return ga.DEFAULT_MAX_FITNESS
        
    controllerAction = simulation.controller.output
    controlEffort = dynSy.max(controllerAction)
    
    settlingTime = dynSy.settling_time(simulation)
    
    fitness = weighting_function(controlEffort, 1, settlingTime, .5)
    
    return fitness
    

popSize = 500
mutP = .01
crossP = .5
tourneySize = 20

selection = ga.tournament(tourneySize)
crossover = ga.single_point(crossP)
mutation = ga.simple_mutation(mutP)

decimalPrecision = 3

integerPart = ga.Nucleotide( GTypes.GInt(min=0, max=1000) )
decimalPart = ga.Nucleotide( GTypes.GInt(min=1, max=10**decimalPrecision-1) )


gain = ga.Gene( [integerPart, decimalPart], lambda x: x[0].data.value+x[1].data.value/(10**decimalPrecision) )

chromosome = ga.Chromosome( [gain for i in range(3)] )
individual = ga.Individual( [chromosome] )

initialPopulation = ga.Population.random( [individual for i in range(popSize)] )
for indiv in initialPopulation:
   print(indiv)
