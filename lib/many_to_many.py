class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.__class__.members.append(self)

    @classmethod
    def all_members(cls):
        return cls.members

    def contracts(self):
        return [contract for contract in Contract.all_members() if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)

    @classmethod
    def all_members(cls):
        return cls.members

    def contracts(self):
        return [contract for contract in Contract.all_members() if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The 'book' parameter must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The 'date' parameter must be a string.")
        if not isinstance(royalties, int):
            raise Exception("The 'royalties' parameter must be an integer.")
        if not 0 <= royalties <= 100:
            raise Exception("Royalties must be between 0 and 100.")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The 'author' parameter must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The 'book' parameter must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The 'date' parameter must be a string.")
        if not isinstance(royalties, int):
            raise Exception("The 'royalties' parameter must be an integer.")
        if not 0 <= royalties <= 100:
            raise Exception("Royalties must be between 0 and 100.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.members.append(self)


    @classmethod
    def all_members(cls):
        return cls.members

    @classmethod
    def contracts_by_date(cls, date):
        return sorted(cls.all_members(), key=lambda x: x.date)


