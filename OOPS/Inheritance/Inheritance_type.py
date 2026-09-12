""" Single-level inheritance 
Parent class = Employee 
child class = Teacher
"""
class Employee:
    start_time = "9am" # default constructor already created here...
    end_time = "6pm"
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
    def get_info(self):
        print(f"Subject name : {self.subject} \nTiming : {self.start_time} - {self.end_time}")
t1 = Teacher("Maths for AI")
# print(t1.subject, t1.start_time, t1.end_time)
t1.get_info()

""" Multi-level inheritance
Employee --> AdminStaff --> Accountant
super() - keyword introduced --> It is used to call superclass (parent class) constructor in his child class. If we are using super() keyword then we need not to use [self parameter] in our code taking or accessing parent properties. But if we are using classname to inherit properties we need [self parameter] to refer current object...
"""
class Employee:
    start_time = "9am"
    end_time = "6pm"
class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
class Accountant(AdminStaff):
    def __init__(self, salary, role): # We have taken role as parameter inside child class initializer/constructor because we are inheritate its parent class property inside it...
        super().__init__(role)
        self.salary = salary
    def get_info(self):
        print(f"Role : {self.role} \nSalary : {self.salary} \nTiming : {self.start_time} - {self.end_time}")
acc1 = Accountant(95_000, "CA")
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)
acc1.get_info()

""" Multiple Inheritance
here there are multiple parent classes are present also there is one child class who inherit there properties and methods
Teacher - Student (both are parent classes) --> TA (Teaching Assistant) (child class)
"""
class Teacher:
    def __init__(self, salary):
        self.salary = salary
class Student:
    def __init__(self, gpa):
        self.gpa = gpa
class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name 
    def info(self):
        print(f"Name : {self.name} \nGPA : {self.gpa} \nSalary : {self.salary}")
ta1 = TA(550_000, 9.4, "Utkarsh")
# print(ta1.name, ta1.gpa, ta1.salary)
ta1.info()