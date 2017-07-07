import random

class RandomGenerator():
    random = random.Random()
    
    def seed(self, seed=None):
        self.random.seed(seed)
    
    def random_int(self, min, max):
        return self.random.randint(min,max)
        
    def random_real(self, min, max):
        return self.random.uniform(min,max)