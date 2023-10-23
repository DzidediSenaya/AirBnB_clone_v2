#!/usr/bin/python3
"""
Starts a Flask web application to display a list of states and their cities.
The application listens on 0.0.0.0 and port 5000.
Uses the storage engine to retrieve data from the database.

Routes:
    /cities_by_states: Display a list of states and their cities.

This script requires that Flask and SQLAlchemy are installed.
"""

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.

    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
