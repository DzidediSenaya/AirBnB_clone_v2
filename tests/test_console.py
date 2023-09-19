#!/usr/bin/python3
"""Defines unittests for console.py."""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import pep8
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.prompt = "(hbnb) "

    def tearDown(self):
        pass

    def test_pep8_conformance(self):
        """Test that console.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 style issues found")

    def test_create_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.isalnum())  # Expecting an alphanumeric ID
            # Check if the object was created and stored in the storage
            obj = storage.all().get("BaseModel.{}".format(output))
            self.assertIsInstance(obj, BaseModel)

    def test_show_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            # Reset the mock stdout
            mock_stdout.truncate(0)
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                self.console.onecmd("show BaseModel {}".format(created_output))
                output = mock_stdout.getvalue().strip()
                # Check if the output contains the created object's information
                self.assertIn(created_output, output)

    def test_destroy_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            # Reset the mock stdout
            mock_stdout.truncate(0)
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                self.console.onecmd("destroy BaseModel {}".format(created_output))
                output = mock_stdout.getvalue().strip()
                # Check if the object was deleted
                self.assertEqual(output, "")

    def test_all_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            # Reset the mock stdout
            mock_stdout.truncate(0)
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                self.console.onecmd("all BaseModel")
                output = mock_stdout.getvalue().strip()
                # Check if the output contains the created object's information
                self.assertIn(created_output, output)

    def test_update_command(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            # Reset the mock stdout
            mock_stdout.truncate(0)
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                self.console.onecmd("update BaseModel {} name 'NewName'".format(created_output))
                output = mock_stdout.getvalue().strip()
                # Check if the object was updated successfully
                self.assertEqual(output, "")

                # Verify if the object was updated in the storage
                updated_obj = storage.all().get("BaseModel.{}".format(created_output))
                self.assertEqual(updated_obj.name, "NewName")

if __name__ == '__main__':
    unittest.main()
