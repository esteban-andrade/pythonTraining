# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title" # this is are the defaults
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func) # default factory will call function to give default value. TO use single value default should be the option 


# Create a default book object
b1 = Book()
print(b1)

# Create a specified book, price is set by field operator
b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
print(b2)
