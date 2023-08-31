#!/usr/bin/python3
""" handles all default RestFul API actions for Genres """
from models.genre import Genre
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/genres/<parent_genre>', methods=['GET'],
                 strict_slashes=False)
def get_genres(parent_genre):
    """
    Retrieves all Genres with the given parent genre
    """

    genre_list = []
    all_genres = storage.all(Genre).values()

    for genre in all_genres:
        if genre.parent_genre == parent_genre:
            genre_list.append(genre.to_dict())

    return jsonify(genre_list)
