class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(f"Name of Person : {self.name} his age is {self.age} and he lives in {self.address}")

print("Printing name only...")    
person = Person("Utkarsh")
person.show()
print("--------------------------------------- \nPrinting name and age...")
person = Person("Utkarsh", 22)
person.show()
print("--------------------------------------- \nPrinting name, age and address...")
person = Person("Utkarsh", 22, "USA")
person.show()

""" We used foundational core concept of default parameter - in which we cannot use multiple parameters in a single class but we can use default parameters in a single constructor (None or default values) so that even they are not given value they return None or default value whatever we give except giving error """
