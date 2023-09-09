#!/usr/bin/python3
""" handles all default RestFul API actions for Genres """
from models.genre import Genre
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/genres/<parent_genre>', methods=['GET'],
                 strict_slashes=False)
def get_genres(parent_genre):
    """
    Retrieves all Genres with the given parent genre
    """

    # Define list variable that will be returned by function
    # and retrieve all Genre objects from the database
    genre_list = []
    all_genres = list(storage.all(Genre).values())

    # Iterate through objects retrieved from database
    # and append to `genre_list` all objects whose
    # `parent_genre` attribute matches the given parameter
    for genre in all_genres:
        if genre.parent_genre == parent_genre:
            genre_list.append(genre.to_dict())

    # Return `genre_list` in JSON string format for response
    return jsonify(genre_list)
