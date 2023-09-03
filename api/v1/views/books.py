#!/usr/bin/python3
""" handles all default RestFul API actions for Books """
from models.book import Book
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request
from random import randint


@app_views.route('/books/random', methods=['GET'], strict_slashes=False)
def get_random_book():
    """
    retrieves a random book from the database
    """
    # Retrieve all books from database
    all_books = list(storage.all(Book).values())

    # Find the length of the list to use as range for randint
    length = len(all_books)

    # Use randint to pick a random index to retrieve a random book
    random_idx = randint(0, length - 1)
    random_book = all_books[random_idx]

    # Return random book
    return jsonify(random_book.to_dict())


@app_views.route('/books', methods=['POST'], strict_slashes=False)
def get_books_list():
    """
    Fetches books based on given book_ids
    """
    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        book_ids_list = data.get('book_ids', None)

    if not book_ids_list:
        abort(400, description="Not a JSON")

    books_list = []

    # Iterate through book_ids and retrieve books
    for book_id in book_ids_list:
        book = storage.get(Book, book_id)
        books_list.append(book.to_dict())

    return jsonify(books_list)


@app_views.route('/recommended_books', methods=['POST'], strict_slashes=False)
def get_recommended_books():
    """
    Retrieves Book objects depending of the JSON in the body
    of the request
    """
    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        age_categories = data.get('age_categories', None)
        book_lengths = data.get('book_lengths', None)
        genres = data.get('genres', None)

    recommended_books = []

    books = list(storage.all(Book).values())

    if not data or not len(data) or (
            not age_categories and
            not book_lengths and
            not genres):
        for book in books:
            recommended_books.append(book.to_dict())

        return jsonify(recommended_books)

    for book in books:
        if genres:
            flag = False
            book_genres = book.genres
            book_genre_ids = [genre.id for genre in book_genres]
            for genre in genres:
                if genre not in book_genre_ids:
                    flag = True
                    break
            if flag:
                continue
        if book_lengths:
            book_length = ""
            if book.page_length < 200:
                book_length = "Short"
            elif book.page_length >= 200 and book.page_length < 500:
                book_length = "Mid-length"
            else:
                book_length = "Long"
            if book_length not in book_lengths:
                continue
        if age_categories:
            if book.age_category not in age_categories:
                continue

        book_dict = book.to_dict()
        book_dict.pop("genres", None)
        recommended_books.append(book_dict)

    return jsonify(recommended_books)
