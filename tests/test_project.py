import unittest
import sys
import os

# Add the parent directory to sys.path to import project module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.models.project import Project

class TestProject(unittest.TestCase):
    """Unit tests for the Project class."""

    def setUp(self):
        """Set up a Project instance for testing."""
        self.project = Project(
            project_key="TEST",
            project_name="Test Project",
            project_initials="TP",
            project_full_name="Test Project Full Name",
            component_prefix="test_"
        )

    def test_project_key(self):
        """Test the project_key property."""
        self.assertEqual(self.project.project_key, "TEST")
        self.project.project_key = "NEW"
        self.assertEqual(self.project.project_key, "NEW")

    def test_project_name(self):
        """Test the project_name property."""
        self.assertEqual(self.project.project_name, "Test Project")
        self.project.project_name = "New Name"
        self.assertEqual(self.project.project_name, "New Name")

    def test_project_initials(self):
        """Test the project_initials property."""
        self.assertEqual(self.project.project_initials, "TP")
        self.project.project_initials = "NN"
        self.assertEqual(self.project.project_initials, "NN")

    def test_project_full_name(self):
        """Test the project_full_name property."""
        self.assertEqual(self.project.project_full_name, "Test Project Full Name")
        self.project.project_full_name = "New Full Name"
        self.assertEqual(self.project.project_full_name, "New Full Name")

    def test_component_prefix(self):
        """Test the component_prefix property."""
        self.assertEqual(self.project.component_prefix, "test_")
        self.project.component_prefix = "new_"
        self.assertEqual(self.project.component_prefix, "new_")

    def test_str(self):
        """Test the __str__ method."""
        expected_str = "TEST - Test Project - TP - Test Project Full Name - test_"
        self.assertEqual(str(self.project), expected_str)

if __name__ == '__main__':
    unittest.main()
