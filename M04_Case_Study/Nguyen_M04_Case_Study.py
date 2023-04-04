from flask import Flask 
import requests
app = Flask(__name__) # set up flask app
from flask_sqlalchemy import SQLAlchemy # import sql alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # configure database so that we can connect to it
db = SQLAlchemy(app) 

# Create a model for the relational database
class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_name = db.Column(db.String(80), nullable=False)
	author = db.Column(db.String(80), nullable=False)
	publisher = db.Column(db.String(80), nullable=False)

	# function prints out string representation of Book model  
	def __str__(self):
		return f"'{self.book_name}' by {self.author} - Publisher: {self.publisher}"

# Path or endpoint for home page
@app.route('/')
def index():
	return "Home Books"

# Functions for getting our get requests and sending responses for users
@app.route('/books')
def get_books():
	books = Book.query.all() # get all book objects from database
	# Loop through all books, but them in a dictionary/map/object, put those in an array. Finally return array of books 
	output = []
	for book in books:
		# Has to be in json notation, which works if it's dictionaries
		book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}
		output.append(book_data)
	return {"books": output}
 
# Query books based on the id of the book
@app.route('/books/<id>') # 
def get_book(id):
	book = Book.query.get_or_404(id)
	return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

# Adding books to the database by using POST http request
@app.route('/books', methods=["POST"])
def add_book():
	book = Book(book_name=requests.json['book_name'], author=requests.json['author'], publisher=requests.json['publisher'])

	db.session.add(book) # database tracks book from the session
	db.session.commit() # saves changes and saves books
	return {'id': book.id} # Then we're just going to return book id as a confirmation that it worked

# Deleting books from database using http delete request 
@app.route('/books/<id>')
def delete_book(id):
	book = Book.query.get(id)
	if book is None:
		return {"error": "not found"}
	db.session.delete(book)
	db.session.commit()
	return {"message": f"Book was deleted"}