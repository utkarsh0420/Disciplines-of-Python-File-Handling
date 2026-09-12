"""Reusing attributes and methods from parent (base) class to child class"""

class Employee:
    start_time = "8am"
    end_time = "6pm"

class Teacher(Employee):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def get_info(self):
        return f"Teacher name : {self.name} \nSubject : {self.subject} \nTiming : {self.start_time} - {self.end_time}"

t1 = Teacher("Nishant Vora", "Mathematics")
# print(t1.name, t1.subject, t1.start_time, t1.end_time)
print(t1.get_info())
