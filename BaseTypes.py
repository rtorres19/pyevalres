# BaseTypes.py
import abc
from . import GRandom
from .Utility import map_and_str, compare_iterables_by_element

randomGenerator = GRandom.RandomGenerator()

def seed(seed=0):
    randomGenerator.seed(seed)

class Container(object):
    def __init__(self, elements):
        self._elements = tuple(iter(elements))
    
    @property
    def elements(self):
        return Container(self._elements)

    def append(self, container):
        try:
            newElements = (self._elements + container._elements)
        except AttributeError:
            elements = container
            try:
                newElements = (self._elements + elements)
            except TypeError:
                element = elements
                newElements = (self._elements + (element, ))
        return type(self)(newElements)
        
    def insert_at_end(self, element):
        newElements = (self._elements + (element, ))
        return type(self)(newElements)
    
    def sort(self, sorting_function=None, r=False):
        return type(self)(sorted(self.elements, key=sorting_function, reverse=r))

    def copy(self):
        return type(self)(self._elements)
        
    def __len__(self):
        return len(self._elements)
        
    def __iter__(self):
        return iter(self._elements)
        
    def __getitem__(self, key):
        # slicing returns a Container built from the slice
        if type(key) == slice:
            return type(self)(self._elements[key])
        # indexing returns the element
        return self._elements[key]

    def setitem(self, key, value):
        newContainer = type(self)([])
        # transform a singleton key into a single item tuple:
        if type(key)==int:
            key = (key, )
        # single level set case (base case):
        if len(key)==1:
            for i in range(len(self)):
                if i==key[0]:
                    newContainer = newContainer.insert_at_end(value)
                else:
                    newContainer = newContainer.insert_at_end(self[i])
            return newContainer
        # nested key set case:
        else:
            for i in range(len(self)):
                if i==key[0]:
                    newElement = self[key[0]].setitem(key[1:], value)
                    newContainer = newContainer.insert_at_end(newElement)
                else:
                    newContainer = newContainer.insert_at_end(self[i])
            return newContainer
            
    def setslice(self, i, j, values):
        aux = self
        for k in range(i,j):
            aux = aux.setitem(k,values[k-i])
        return aux

    def __eq__(self, other):
        try:
            return self._elements==other._elements
        except AttributeError:
            return compare_iterables_by_element(self, other)

    def __contains__(self, element):
        return element in self._elements

    def __str__(self):
        return map_and_str(str, self, '(', ')')
        
    def __repr__(self):
        return repr(self._elements)

class Limiter(object):
    @abc.abstractmethod
    def __contains__(self, value):
        pass

    @abc.abstractmethod
    def get_random_value(self):
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass

class Interval(Limiter):
    def __init__(self, min, max):
        if min>=max:
            raise TypeError("Minimum limit must be less than maximum limit")
        
        self._min = min
        self._max = max

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max
    
    def __contains__(self, value):
        return value>=self.min and value<=self.max

    def __eq__(self, other):
        return (type(self)==type(other) and 
                self.min==other.min and self.max==other.max)

    def __str__(self):
        return '({},{})'.format(str(self.min), str(self.max))

    def __repr__(self):
        return '{}({},{})'.format(type(self).__name__, 
                                  str(self.min), 
                                  str(self.max))
        
class IntInterval(Interval):
    def __init__(self, min, max):
        super().__init__(min, max)

    def __contains__(self, value):
        return isinstance(value, int) and super().__contains__(value)

    def get_random_value(self):
        return randomGenerator.random_int(self.min, self.max)

class FloatInterval(Interval):
    def __init__(self, min, max):
        super().__init__(min, max)

    def __contains__(self, value):
        return ((isinstance(value, float) or isinstance(value, int)) 
                 and super().__contains__(value))

    def get_random_value(self):
        return randomGenerator.random_real(self.min, self.max)

class Set(Limiter):
    def __init__(self, members):
        self._members = set(members)

    @property
    def members(self):
        return self._members

    def __contains__(self, value):
        return value in self.members

    def get_random_value(self):
        return randomGenerator.random_choice(list(self.members))
    
    def __eq__(self, other):
        return self._members==other._members

    def __str__(self):
        return str(self.members)

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, str(self.members))

class CharSet(Set):
    def __init__(self, members):
        super().__init__(members)

    @property
    def members(self):
        aux = list(self._members)
        aux.sort()
        return aux

    def __eq__(self, other):
        try:
            return super().__eq__(other)
        except AttributeError:
            return self._members == set(other)

    def __str__(self):
        return '({})'.format(repr(''.join(self.members)))

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, 
                               repr(''.join(self.members)))

class LimitedValue(object):
    def __init__(self, value=None, domain=None):
        if domain is None:
            raise TypeError("domain needs to be explicitly specified")
        if not isinstance(domain, Limiter):
            raise TypeError("Type of domain not specified")

        self._domain = domain
        if value is None:
            self._value = self.domain.get_random_value()
        elif self.isindomain(value):
            self._value = value
        else:
            raise ValueError("Value is not in the set of valid values")

        if isinstance(self.domain, Interval):
            type(self).min = property(lambda self: self.domain.min)
            type(self).max = property(lambda self: self.domain.max)

        elif isinstance(self.domain, Set):
            type(self).set = property(lambda self: self.domain.members)

    @property
    def value(self):
        return self._value

    @property
    def domain(self):
        return self._domain
        
    def isindomain(self, value):
        return value in self.domain
        
    def get_random_value(self):
        return self.domain.get_random_value()
        
    def copy(self):
        return type(self)(self.value, self.domain)

    def __str__(self):
        return '{} in {}'.format(str(self.value), str(self.domain))
        
    def __eq__(self, other):
        return self.domain==other.domain and self.value==other.value

    def __repr__(self):
        return '{}({},{})'.format(type(self).__name__,
                                  repr(self.value),
                                  repr(self.domain))
