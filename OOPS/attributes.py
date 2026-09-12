class Student:
    college_name = "IIT Bombay"

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):   #self - it referes to current object
        print(f"Name : {self.name}")
        print(f"& Age : {self.age}") 

stu1 = Student("Utkarsh",23)  # object creation
stu1.display()
print(stu1.name)
print(stu1.age)
print(stu1.college_name)
print(Student.college_name)  #using class name for calling

