#-------------------class & instance attributes-------------__init__ function---------------------------#

# class Student:        
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in the database")
# print("Database : ")
# s1 = Student("Utkarsh", 95)
# print(s1.name, s1.marks)
# s2 = Student("Tony", 94)
# print(s2.name, s2.marks)

# class Student:
#     college_name = "ABC college"
#     name = "anonymous"
#     def __init__(self, marks ,name=name):
#         self.name = name
#         self.marks = marks
#         print("Adding new database :")
# s1 = Student("Tony", 95)
# print(s1.name, s1.marks)
# s2 = Student(36)
# print(s2.name, s2.marks)

#-------------------------Methods-------------------------------------#

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def hello(self):  # Method/Function
#         print("Hello,", self.name)
        
# s1 = Student("Utkarsh")
# s1.hello()  # calling method

            # Linear Search #
# nums = [1,2,3,10,5,6,7,8]
# target = int(input("Enter a target number :"))
# index = 0
# for i in nums:
#     if (i == target):
#         print(f"{target} found at index : {index}")
#         break
#     index += 1



# class Book:
#     count = 0
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.reviews = []

#     def add_reviews(self, review_text, ratings):
#         if 1 <= ratings <= 5:
#             review_data = {
#                 "Review Text" : review_text,
#                 "Ratings" : ratings 
#             }
#             self.reviews.append(review_data)
#             Book.count += 1
#             print(f"Review added to the {self.title}")
#         else:
#             print("Review should be between 1 to 5 only")
    
#     def show_reviews(self):
#         print(f"All reviews : {self.reviews}")

#     @classmethod
#     def review_count(cls):
#         print(f"Count of reviews : {cls.count}")

# my_b1 = Book("Machines of Loving Garce", "Dario Amodei")
# my_b1.add_reviews("Machine vision", 5)
# my_b1.show_reviews()
# my_b2 = Book("JARVIS", "Tony Stark")
# my_b2.add_reviews("Ai assitant", 5)
# my_b2.show_reviews()
# Book.review_count()  
