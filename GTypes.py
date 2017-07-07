import abc
import GDefaults
import GRandom
from Utility import turn_iterable_to_string_using

randomGenerator = GRandom.RandomGenerator()

def seed(seed=0):
    randomGenerator.seed(seed)
    
class GType():
    pass
    
class MinMaxValue(GType):
    def __init__(self, value, min, max):
        self.min = min
        self.max = max
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if value==None:
            self._value = type(self).random_value(self.min, self.max)
        else:
            if self.isvalid(value):
                self._value = value
            else:
                raise OverflowError
        
    @abc.abstractmethod
    def isvalid(self, value):
        pass
        
    def isininterval(self, value):
        if value>=self.min and value<=self.max:
            return True
        else:
            return False
    
    @staticmethod
    @abc.abstractmethod
    def random_value(min, max):
        pass
        
    def copy(self):
        return type(self)(self.value, self.min, self.max)
        
    def new_random_value(self):
        self.value = type(self).random_value(self.min, self.max)
    
    def isinsameinterval(self, x):
        if (self.min==x.min and self.max==x.max):
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.value)
        
    def __repr__(self):
        return "Value = "+str(self.value)+", Min = "+str(self.min)+", Max = "+str(self.max)+"\n"
        
    def __eq__(self, x):
        if (self.isinsameinterval(x) and self.value==x.value):
            return True
        else:
            return False
        
class GInt(MinMaxValue):
    def __init__(self, value=None, min=GDefaults.GIntMin, max=GDefaults.GIntMax):
        super().__init__(value, min, max)
        
    def isvalid(self, value):
        if not isinstance(value, int):
            return False            
        
        if self.isininterval(value):
            return True
        else:
            return False
        
    @staticmethod
    def random_value(min, max):
        return randomGenerator.random_int(min, max)
        
class GReal(MinMaxValue):
    def __init__(self, value=None, min=GDefaults.GRealMin, max=GDefaults.GRealMax):
        super().__init__(value, min, max)
        
    def isvalid(self, value):
        if not (isinstance(value,float) or isinstance(value,int)):
            return False
        
        if self.isininterval(value):
            return True
        else:
            return False
        
    @staticmethod
    def random_value(min, max):
        return randomGenerator.random_real(min, max)
    
class GContainer(GType):
    """ Attr:
            elements: The list containing the data
            
        Methods:
            ga_repr(): Returns the GA representation of the list, element by element
            ga_prep(): Return the pretty GA representation of the list
            append(elem): Appends an element
            sort(sorting_function, r=False): Sorts its elements using sorting_function.
                r=True for reverse sorting
            __len__()
            __iter__()
    """
    # -------------Init-------------
    def __init__(self, elements):
        self.elements = elements
        
    # ----------Properties----------
    @property
    def elements(self):
        return self._elements
    @elements.setter
    def elements(self, elements):
        self._elements = elements
        
    # -----------Methods------------
    def ga_repr(self):
        """ Returns the GA representation of the container.
        """
        ga_repr_caller = lambda obj: obj.ga_repr()
        return turn_iterable_to_string_using(self, ga_repr_caller)
        
    def ga_prepr(self):
        """ Returns the pretty GA representation of the container.
        """
        ga_prepr_caller = lambda obj: obj.ga_prepr()
        return turn_iterable_to_string_using(self, ga_prepr_caller)
        
    def append(self, element):
        self.elements.append(element)
        
    def sort(self, sorting_function, r=False):
        self.elements.sort(key=sorting_function, reverse=r)
        
    def __len__(self):
        return len(self.elements)
        
    def __iter__(self):
        return iter(self.elements)
        
    def __getitem__(self, key):
        return self.elements[key]
        
    def __setitem__(self, key, value):
        self.elements[key] = value
        
    def __str__(self):
        return turn_iterable_to_string_using(self, str)
        
    def __repr__(self):
        return repr(self.elements)
