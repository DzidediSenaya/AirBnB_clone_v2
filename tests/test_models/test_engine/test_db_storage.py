#!/usr/bin/python3
"""Defines unnittests for models/engine/db_storage.py."""
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from os import getenv


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "Not testing DBStorage")
class TestDBStorage(unittest.TestCase):
    """Unit tests for the DBStorage class."""

    @classmethod
    def setUpClass(cls):
        """Setup the DBStorage instance for testing."""
        cls.storage = DBStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing."""
        del cls.storage

    def test_all(self):
        """Test the 'all' method."""
        # Add an object to the session and save it
        obj = BaseModel()
        obj.save()

        # Ensure that 'all' returns a dictionary containing the object
        result = self.storage.all()
        self.assertIsInstance(result, dict)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", result)

    def test_new(self):
        """Test the 'new' method."""
        # Create an object and add it to the session using 'new'
        obj = BaseModel()
        self.storage.new(obj)

        # Ensure that the object is in the current session
        self.assertIn(obj, self.storage._DBStorage__session)

    def test_save(self):
        """Test the 'save' method."""
        # Create an object and add it to the session using 'new'
        obj = BaseModel()
        self.storage.new(obj)

        # Save the session and check if the object is in the database
        self.storage.save()
        result = self.storage._DBStorage__session.query(BaseModel).get(obj.id)
        self.assertIsNotNone(result)

    def test_delete(self):
        """Test the 'delete' method."""
        # Create an object, add it to the session, and then delete it
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.delete(obj)

        # Ensure that the object is removed from the session
        self.assertNotIn(obj, self.storage._DBStorage__session)

    def test_reload(self):
        """Test the 'reload' method."""
        # Reload the database and ensure that the session is cleared
        self.storage.reload()
        self.assertIsNone(self.storage._DBStorage__session)

if __name__ == "__main__":
    unittest.main()
