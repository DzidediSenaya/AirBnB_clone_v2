#!/usr/bin/python3
"""This script starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name)

# Fetch the necessary data from the storage
states = storage.all(State)
cities = storage.all(City)
amenities = storage.all(Amenity)
places = storage.all(Place)

# Sort the data by name (A->Z)
states = sorted(states.values(), key=lambda state: state.name)
cities = sorted(cities.values(), key=lambda city: city.name)
amenities = sorted(amenities.values(), key=lambda amenity: amenity.name)
places = sorted(places.values(), key=lambda place: place.name)


# Route to display the HTML page
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display an HTML page like 8-index.html."""
    return render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    )


# Tear down the session after each request
@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
