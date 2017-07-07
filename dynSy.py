class DynamicSystem(object):
    
    def __init__(self, state_derivatives, initialTime=None, initialConditions=None):
        self.state_derivatives = state_derivatives
        self.initialTime = initialTime
        self.initialConditions = initialConditions
        
    def __call__(self, finalTime, initialConditions=self.initialConditions):
        return numericSolver.solve(self.state_derivatives, initialTime, initialConditions, finalTime)