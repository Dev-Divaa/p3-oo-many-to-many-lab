class Book:
    all_books = []  # Class variable to keep track of all books

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)  # Add book to the class variable list

    def __str__(self):
        return f"Book title: {self.title}"

class Author:
    all_authors = []  # Class variable to keep track of all authors

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)  # Add author to the class variable list
        self._contracts = []  # Instance variable to keep track of contracts

    def __str__(self):
        return f"Author name: {self.name}"

    # Method to return all related contracts
    def contracts(self):
        return self._contracts

    # Method to return all related books through contracts
    def books(self):
        return [contract.book for contract in self._contracts]

    # Method to sign a new contract
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")
        
        contract = Contract(self, book, date, royalties)  # Create a new contract
        self._contracts.append(contract)  # Add to the author's contracts
        return contract

    # Method to calculate total royalties earned
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Contract:
    all_contracts = []  # Class variable to keep track of all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)  # Add contract to the class variable list

    def __str__(self):
        return f"Contract for {self.book.title} by {self.author.name} on {self.date}, Royalties: {self.royalties}%"

    # Class method to return contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

# Example usage:
author1 = Author("F. Scott Fitzgerald")
book1 = Book("The Great Gatsby")
book2 = Book("Tender is the Night")

# Signing contracts
contract1 = author1.sign_contract(book1, "2024-09-01", 15)
contract2 = author1.sign_contract(book2, "2024-10-15", 20)

# Output contracts
print(author1.contracts())  # List of contracts for the author
print(author1.books())  # List of books for the author
print(f"Total Royalties: {author1.total_royalties()}%")  # Total royalties

# Find contracts by date
contracts_on_date = Contract.contracts_by_date("2024-09-01")
print(contracts_on_date)
