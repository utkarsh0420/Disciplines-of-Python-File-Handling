""" Polymorphism 
- many forms
- multiple function --> same name
- operator overloading --> + (add, concatenation) same operator diffrent working
1. Function overriding - follows inheritance and redefining parent class function in child class
2. Duck Typing - no inheritance
"""
""" 1. Function Overriding """
# class Employee:
#     def __init__(self):
#         print("Designation = Employee")
# class Teacher(Employee):
#     def __init__(self):
#         print("Designation = Teacher")
# t1 = Teacher()
# t1.__init__() # ofcourse after calling __init__() it being called because it is also a function or we can say it is initializer i.e. constructor...
""" Here in line 11 and line 14 actually function overriding is occurring that's why after creation of t1 object and calling method it called latest one """
# Same with get_designation() method
""" We are taking self in place of parameter because it is instance method which have a property that it should compulsory contain one parameter self in it and can contain mutiple too also self refers to current object """
# class Employee:
#     def get_designation(self):
#         print("Designation = Employee")
# class Teacher(Employee):
#     def get_designation(self):
#         print("Designation = Teacher")
# t1 = Teacher()
# t1.get_designation()
""" __init__ is an automatic constructor method whereas get_designation() is custom method. Therfore when i wrote t1 = Teacher() it created an object and triggered automatically and for t1.__init__() it is being called manually so 2 times output shown on screen """
# Main focus must be on foundational cores that is what used to build coding logic and even to build model...

""" 2. Duck Typing 
No inheritance involved
"""
class Teacher:
    def get_designation(self):
        print("Designation = Teacher")
class Accountant:
    def get_designation(self):
        print("Designation = Accountant")
t1 = Teacher()
t1.get_designation()
acc1 = Accountant()
acc1.get_designation()
