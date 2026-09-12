# class Student:
#     def __init__(self, name, roll_no, marks):  # Initializer / constructor 
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
    
#     @property
#     def get_details(self):  # getter method
#         return self.__name, self.__roll_no, self.__marks
    
#     @get_details.setter
#     def set_marks(self, m):
#         if m<0:
#             raise ValueError("Marks can't be negative")
#         self.__marks = m

#     @get_details.setter 
#     def set_roll(self, r):
#         if 1 <= r <= 100:
#             self.__roll_no = r
#             print(f"Roll no: {self.__roll_no}")
#         else:
#             raise ValueError("Roll number must be between 1 to 100")
            
#     @get_details.setter
#     def set_name(self, n):
#         if not n or not str(n).strip():
#             raise ValueError("Name cannot be empty!!")
#         self.__name = n
        
""" Up side script was my logic which is partially wrong with some syntax error """
""" setter is used to store the data """
""" Without decorator code """
class Student:
    def __init__(self, name, roll_no, marks):
        self.set_details(name, roll_no, marks)
    
    def set_details(self, name, roll_no, marks): # Setter
        # Name validation
        if not name or not str(name).strip():
            raise ValueError("Name cannot be empty")
        
        # Roll no validation
        if not (1 <= roll_no <= 100):
            raise ValueError("Roll number should lie between 1 to 100 only")

        # Marks validation
        if marks<0:
            raise ValueError("Marks can't be negative")

        # After all validations
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_details(self):
        return self.__name, self.__roll_no, self.__marks

name = input("Enter your name :")
roll_no = int(input("Enter a roll number :"))
marks = int(input("Enter marks :"))
s1 = Student(name, roll_no, marks)
print(f"Student details : {s1.get_details()}")


""" With decorator """
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def roll_no(self):
        return self.__roll_no
    
    @roll_no.setter
    def roll_no(self, r):
        if not (1<=r<=100):
            raise ValueError("Roll numbers should be between 1 to 100")
        self.__roll_no = r

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self, m):
        if m<0:
            raise ValueError("Marks cannot be negative")
        self.__marks = m

    def show_info(self):
        return self.__name, self.__roll_no, self.__marks

name = input("Enter your name :")
roll_no = int(input("Enter your Roll number :"))
marks = int(input("Enter your marks :"))
s1 = Student(name, roll_no, marks) 
print(s1.show_info())
