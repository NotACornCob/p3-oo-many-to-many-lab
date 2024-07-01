from datetime import datetime
import ipdb 

class Author:

    all = []

    def __init__(self,name):
        self.name = name
        self.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [book for book in Book.all if book.author == self]
    def sign_contract(book,date,royalties):
        return Contract.all.append(book,date,royalties)
    def total_royalties():
        return [royalty for royalty in Contract.all if royalty.author == Author]

class Book:

    all = []

    def __init__(self,title):
        self.title = title
        self.all.append(self)

class Contract:

    all = []

    def __init__(self, author, book, date = datetime.now(), royalties = "40000"):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @property 
    def author(self):
        self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author,str):
            self._author = author
        else:
            raise Exception("Nope")

    @property 
    def book(self):
        self._book

    @book.setter
    def book(self,book):
        if isinstance(book,str):
            self._book = book
        else: 
            raise Exception("Nope")

    @property
    def date(self):
        self._date

    @date.setter
    def date(self,date):
        self._date = date
    
    @property
    def royalties(self):
        self._royalties

    @royalties.setter
    def royalties (self,royalties):
        self._royalties = royalties

Guy = Author("Guy")
BestEver = Book("BestEver")
Contract1 = Contract(Guy,BestEver)
print(Guy.name)
print(BestEver.title)
print(Contract.all)