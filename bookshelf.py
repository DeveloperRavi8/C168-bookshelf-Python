from datetime import date
class Bookshelf():

    def __init__(self):
        self.current_year = date.today().year
        

    def add_book(self, name, author, price, publishing_year):
        self.name = name
        self.author = author
        self.price = price 
        self.publishing_year = publishing_year

        print("Name : "+ self.name)
        print("Author :"+ self.author)
        print("Price : "+ str(self.price))
        print("Publishing Year : "+ str(self.publishing_year))

    def years_since_published(self):
        year = self.current_year - self.publishing_year
        print("This book was published "+ str(year) +" years ago")

intance_of_bookself = Bookshelf()
intance_of_bookself.add_book("Harry Potter and the philosopher's stone", "J.K Rowling", 2000, 1997)
intance_of_bookself.add_book("New Book", "New autor", 2220, 1447)
intance_of_bookself.years_since_published()