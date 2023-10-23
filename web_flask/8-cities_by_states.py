#!/usr/bin/python3
"""
Starts a Flask web application to display a list of states and their cities.
The application listens on 0.0.0.0 and port 5000.
Uses the storage engine to retrieve data from the database.

Routes:
    /cities_by_states: Display a list of states and their cities.

This script requires that Flask and SQLAlchemy are installed.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Handles the /cities_by_states route and renders the HTML template.

    Returns:
        Rendered HTML template with a list of states and cities.
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    Teardown function to close the storage engine's session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
