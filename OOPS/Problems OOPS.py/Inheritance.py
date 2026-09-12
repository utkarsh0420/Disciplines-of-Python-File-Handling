class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, seats, brand, model):
        super().__init__(brand, model)
        self.seats = seats 
    
    def car_info(self):
        print(f"Seats : {self.seats} \nBrand : {self.brand} \nModel : {self.model}")

class Bike(Vehicle):
    def __init__(self, engine_cc, brand, model):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def bike_info(self):
        print(f"Engine cc : {self.engine_cc} \nBrand : {self.brand} \nModel : {self.model}")

print("Car COnfigurations :- ") 
c1 = Car(4, "BMW", "BMW Z4")
c1.car_info()
print("Bike Configurations :- ")
b1 = Bike("999 cc", "BMW S 1000 RR", "PRO M sport")
b1.bike_info()
