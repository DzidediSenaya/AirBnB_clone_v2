#!/usr/bin/python3
"""This script starts a Flask web application."""
from flask import Flask, render_template

app = Flask(__name)


# Routes
@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display an HTML page with filters."""
    # Fetch the data you need from the database
    # You can use storage to fetch State, City, and Amenity objects
    # Sort the data by name (A->Z)
    # Render the '10-hbnb_filters.html' template with the data
    return render_template('10-hbnb_filters.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
