# # # Online store # # #
class Product:
    count = 0

    def __init__(self,name,price): #constructor
        self.name = name 
        self.price = price
        Product.count += 1 #Tracking all products which are being created

    def get_info(self): #instance method - where each product name and price will be unique
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod #Decorator - class method
    def get_count(cls): # cls attribute
        print(f"Total products in store is {cls.count}")

    @staticmethod #Decorator - static method
    def calc_discount(price, discount): # no cls and no self attribute
        print(f"Discounted price is {price - (price*discount/100)}")
    
p1 = Product("Phone", 30_000) #objects creation
p2 = Product("Laptop", 80_000)
p3 = Product("Tablet", 35_000)
p4 = Product("Pen", 10)

p1.get_info()
Product.get_count() #By classname we will take count to track total products created
p1.calc_discount(30_000, 10)
p2.calc_discount(p2.price, 12) # Dynamic price taken while calling function
