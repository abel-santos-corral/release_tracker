import unittest
import sys
import os
from unittest.mock import patch, mock_open

# Add the parent directory to sys.path to import project_service module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.project_service import ProjectService

class TestProjectService(unittest.TestCase):
    """Unit tests for the ProjectService class."""

    @patch('builtins.open', new_callable=mock_open, read_data='{"0": {"Project key": "D8BBI", "Project name": "CBE", "Project initials": "CBE", "Project full name": "Circular Bio-based Europe", "Component prefix": "cbe_"}}')
    @patch('os.path.exists', return_value=True)
    def setUp(self, mock_exists, mock_file):
        """Set up a ProjectService instance for testing."""
        fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'project.json')
        self.service = ProjectService(fixture_path)

    def test_load_projects(self):
        """Test loading projects from the JSON file."""
        self.assertEqual(len(self.service.projects), 1)
        self.assertEqual(self.service.projects[0].project_key, "D8BBI")

    def test_get_component_prefix(self):
        """Test getting the component prefix for a given project key."""
        prefix = self.service.get_component_prefix("D8BBI")
        self.assertEqual(prefix, "cbe_")

    def test_get_component_prefix_nonexistent(self):
        """Test getting the component prefix for a non-existent project key."""
        prefix = self.service.get_component_prefix("NONEXISTENT")
        self.assertIsNone(prefix)

    def test_get_component_prefix_no_key(self):
        """Test getting the component prefix with no project key."""
        prefix = self.service.get_component_prefix(None)
        self.assertIsNone(prefix)

    def test_get_project_mapping(self):
        """Test getting the project mapping."""
        mapping = self.service.get_project_mapping()
        expected_mapping = {"D8BBI": "cbe_"}
        self.assertEqual(mapping, expected_mapping)

    @patch('builtins.open', new_callable=mock_open, read_data='')
    @patch('os.path.exists', return_value=True)
    def test_load_projects_empty_file(self, mock_exists, mock_file):
        """Test loading projects from an empty JSON file."""
        fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'project_empty.json')
        with self.assertRaises(ValueError) as context:
            ProjectService(fixture_path)
        self.assertEqual(str(context.exception), "The JSON file is empty.")

    @patch('os.path.exists', return_value=False)
    def test_load_projects_file_not_found(self, mock_exists):
        """Test loading projects when the file does not exist."""
        fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'project_non_exists.json')
        with self.assertRaises(Exception) as context:
            ProjectService(fixture_path)
        self.assertEqual(str(context.exception), "There has been a problem managing project.json file. Cannot mount application. Please check.")

if __name__ == '__main__':
    unittest.main()
