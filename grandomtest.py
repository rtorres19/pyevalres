import GRandom

randomGenerator = GRandom.RandomGenerator()
randomGenerator.seed(0)

def random_int_test():
    randInt = randomGenerator.random_int(0,10)
    assert(isinstance(randInt, int))
    assert(randInt==6)
    
def random_real_test():
    randReal = randomGenerator.random_real(0.0,10.0)
    assert(isinstance(randReal, float))
    assert(randReal==7.579544029403024)