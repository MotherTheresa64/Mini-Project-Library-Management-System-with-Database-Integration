from database import Database

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_author(self, db):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        db.execute_query(query, (self.name, self.biography))

    @staticmethod
    def get_all_authors(db):
        query = "SELECT * FROM authors"
        return db.fetch_all(query)

class Book:
    def __init__(self, title, author_id, isbn, publication_date):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date

    def add_book(self, db):
        query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
        db.execute_query(query, (self.title, self.author_id, self.isbn, self.publication_date))

    @staticmethod
    def get_all_books(db):
        query = "SELECT * FROM books"
        return db.fetch_all(query)

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def add_user(self, db):
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        db.execute_query(query, (self.name, self.library_id))

    @staticmethod
    def get_all_users(db):
        query = "SELECT * FROM users"
        return db.fetch_all(query)
