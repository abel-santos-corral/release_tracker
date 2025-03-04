# application/project_service.py
import json
import os
from domain.models.project import Project

class ProjectService:
    """A service class for managing Project objects from a JSON file."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.projects = []
        self.load_projects()

    def load_projects(self):
        """Load projects from a JSON file."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                "There has been a problem managing project.json file. "
                "Cannot mount application. Please check."
            )

        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("The JSON file is empty.")

            try:
                data = json.loads(content)
                if isinstance(data, dict) and not data:
                    raise ValueError("The JSON file contains no data.")
                elif isinstance(data, list) and not data:
                    raise ValueError("The JSON file contains no data.")
            except json.JSONDecodeError:
                raise ValueError("The JSON file is not valid.")

            for entry in data.values():
                project = Project(
                    project_key=entry["Project key"],
                    project_name=entry["Project name"],
                    project_initials=entry["Project initials"],
                    project_full_name=entry["Project full name"],
                    component_prefix=entry["Component prefix"]
                )
                self.projects.append(project)

    def get_component_prefix(self, project_key):
        """
        Get the component prefix for a given project key.

        Args:
            project_key (str): The key of the project to look up.

        Returns:
            str or None: The component prefix if found, otherwise None.
        """
        if not project_key:
            return None

        for project in self.projects:
            if project.project_key == project_key:
                return project.component_prefix

        return None

    def get_project_mapping(self):
        """
        Get a mapping of project keys to component prefixes.

        Returns:
            dict: A dictionary mapping project keys to component prefixes.
        """
        return {project.project_key: project.component_prefix for project in self.projects}
