from .model import Fitness_function

# system_simulation functions:
def identity_simulation(fenotype):
    return fenotype

# evaluate_solution factories:
def make_same_number_evaluation(number, imperfectnessWeight=1/1000):
    def same_number_evaluation(numbers):
        numberCount = numbers.count(number)
        perfectSum = number*len(numbers)
        imperfectness = abs(perfectSum - sum(numbers))
        fitness = numberCount-(imperfectness*imperfectnessWeight)
        return fitness
    return same_number_evaluation

def make_quad_error_same_number_evaluation(number):
    def quad_error_evaluation(numbers):
        error = 0
        for n in numbers:
            error += (number - n)**2
        return error
    return quad_error_evaluation


# fitness_functions factories:
def make_same_number_fitness(number, imperfectnessWeight = 1/1000):
    return Fitness_function(identity_simulation,
                            make_same_number_evaluation(number,
                                                        imperfectnessWeight))
