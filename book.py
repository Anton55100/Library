import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = self._validate_year(year)

    def _validate_year(self, year):
        current_year = datetime.datetime.now().year
        while True:
            try:
                year = int(year)
                if year < 0:
                    print("Year must be a greater or equal than zero.")
                    year = input("Enter book year: ")
                elif year > current_year:
                    print("Year cannot be greater than the current year.")
                    year = input("Enter book year: ")
                else:
                    return year
            except ValueError:
                print("Year must be a number.")
                year = input("Enter book year: ")

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
