class Herbivore:
    def __init__(self, herbivores):
        self.herbivores = herbivores

class Carnivore:
    def __init__(self, food):
        self.food = food

class Omnivore:
    def __init__(self, sound):
        self.sound = sound

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, herbivores, food, sound, type_of):
        super().__init__(herbivores)
        Carnivore.__init__(self, food)
        Omnivore.__init__(self, sound)
        self.type_of  = type_of

    def exact_feature(self):
        print(f"Animal is {self.herbivores} he eats {self.food} and he sounds as {self.sound} also it is {self.type_of}")
    
bear = Bear("Vegeterian", "honey", "growls", "Jungle bear")
bear.exact_feature()
