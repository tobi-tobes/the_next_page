#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template
from models import storage
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/the_next_page', strict_slashes=False)
def tnp_home():
    """ The Next Page is Alive!!! """
    return render_template('home.html', cache_id=uuid.uuid4())


@app.route('/the_next_page/about', strict_slashes=False)
def tnp_about():
    """ About the contributors """
    return render_template('about.html', cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
