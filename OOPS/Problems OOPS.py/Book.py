class Book:
    count = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review_text, ratings):
        if 1 <= ratings <= 5:
            review_data = {
                "Review Text" : review_text,
                "Ratings" : ratings
            }
            self.reviews.append(review_data)
            Book.count += 1
            print(f"Reviews data added successfully")
        else:
            print("Review must be between 1 to 5")
    
    def show_reviews(self):
        print(f"All reviews : {self.reviews}")

    @classmethod
    def count_reviews(cls):
        print(f"Total reviews count : {cls.count}")
    
my_b1 = Book("MAchine of loving grace", "Dario Amodei")
my_b1.add_review("Machine Vision", 4)
my_b1.show_reviews()
my_b2 = Book("JARVIS AI", "Tony stark")
my_b2.add_review("Ai assitant", 5)
my_b2.show_reviews()
Book.count_reviews()