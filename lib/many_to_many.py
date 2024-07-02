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
        return [contract.book for contract in Contract.all if contract.author == self]
    def sign_contract(self,book,date,royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])
    

class Book:
    all = []

    def __init__(self,title):
        self.title = title
        self.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []

    def __init__(self, author, book, date = datetime.now(), royalties = "40000"):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


    @property 
    def author(self):
       return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author
            author.all.append(self)
        else:
            raise TypeError("Invalid author. Expected instance of Author class.")

    @property 
    def book(self):
       return self._book

    @book.setter
    def book(self,book):
        if isinstance(book,Book):
            self._book = book
            book.all.append(self)
        else: 
            raise TypeError("Invalid book. Expected instance of Book class.")

    @property
    def date(self):
       return self._date

    @date.setter
    def date(self,date):
        if isinstance(date,str):
            self._date = date
        else: 
            raise TypeError("Invalid date. Expected data type 'string'.")
    
    @property
    def royalties(self):
       return self._royalties

    @royalties.setter
    def royalties (self,royalties):
        if isinstance (royalties,int):
            self._royalties = royalties
        else: 
            raise TypeError("Invalid input. Royalties must be integers.")


author = Author("Guy")
book = Book("The Good Book")
contract = Contract(author,book,"9/9/9",9000)
contract = author.sign_contract(book, "9/9/9",9000)
print(author.contracts())
print(author.books())
print(Contract.all)