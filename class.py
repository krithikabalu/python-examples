class Book:
	def __init__(self, name, author, year, price):
		self.name = name
		self.author = author
		self.year = year
		self.price = price

	def details(self):
		return "The book {} is written by {} and published in {}. Price of the book is {}".format(self.name, self.author, self.year, self.price)

book = Book("Wings of Fire", "Dr. APJ Abdul Kalam", 1999, 250)
print(book.details())
