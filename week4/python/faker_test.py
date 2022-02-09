from faker import Faker
from math import pi

fake = Faker()
print(fake.date())
print(f'{fake.last_name()} is working {fake.company()} since {fake.date()} and he {fake.text()}')
class Currency:
    def __init__(self, name, amount):
        self.type =name
        self.amount=amount

    def __str__(self):
        return f'{self.amount} {self.type}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.type}s'

    def __add__(self, other):
        if self.type == other.type:
            return int(self)+int(other)
        else:
            raise TypeError(f'Cannot add between Currency type {self.type} and {other.type}')

    def __iadd__(self, n):  
        return self.amount+int(n)


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
'''
print(str(c1))
print(int(c1))
print(c1)
print(c1+c2)

print(c1+c3)
'''

class Circle:
    def __init__(self, radius=0, diameter=0):
        self.radius=radius
        self.diameter = diameter

    def __repr__(self):
        return f'Hello this is circle '
    
    def __add_(self, other):
        return 'addition'

    def __gt__(self, other):
        if self.radius > other.radius:
            return '{self} is bigger'

    def __eq__(self, other):
        if self.radius == other.radius:
            return 'those circles are equal'

    def area(self):
        if self.diameter == 0 :
            return pi*self.radius**2
        elif self.radius == 0 :
            return pi*(self.diameter/2)**2
    

c1= Circle(diameter=6)


