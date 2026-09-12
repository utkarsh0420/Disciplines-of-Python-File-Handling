""" Abstraction
- Hiding internal details and showing only essential features
- Abstraction classes --> Blueprint for other classes
- In parent class we don't make actual implementation because in these cases parent class cannot have or make it generalized instead it's child class inherits its properties as a blueprint and use it...
- example here :- Animal(parent class) --> Lion, Cat, Cow as their child classes (who inherits Animal class method which is not generalized for all like def make_sound(self) method for all other child classes like cat, cow, lion for their sounds)
- abc module --> Abstraction Based Classes :- We use this to import abc and use it for abstraction
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod # It is decorator which is used to tell python that it is abstract method 
    def make_sound(self): 
        pass # Here we are hiding data...
class Lion(Animal):
    def make_sound(self): # And here we are showing only essential features/information... 
        print("Lion sound : Roar...!")
class Cat(Animal):
    def make_sound(self):
        print("Cat sound : Meow...!")
lion = Lion()
lion.make_sound() # calling method
cat = Cat()
cat.make_sound() 
