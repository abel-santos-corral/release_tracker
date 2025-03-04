class Project:
    """A class representing a Project with various attributes."""

    def __init__(self, project_key, project_name, project_initials, project_full_name, component_prefix):
        self._project_key = project_key
        self._project_name = project_name
        self._project_initials = project_initials
        self._project_full_name = project_full_name
        self._component_prefix = component_prefix

    @property
    def project_key(self):
        """Get the project key."""
        return self._project_key

    @project_key.setter
    def project_key(self, value):
        """Set the project key."""
        self._project_key = value

    @property
    def project_name(self):
        """Get the project name."""
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        """Set the project name."""
        self._project_name = value

    @property
    def project_initials(self):
        """Get the project initials."""
        return self._project_initials

    @project_initials.setter
    def project_initials(self, value):
        """Set the project initials."""
        self._project_initials = value

    @property
    def project_full_name(self):
        """Get the project full name."""
        return self._project_full_name

    @project_full_name.setter
    def project_full_name(self, value):
        """Set the project full name."""
        self._project_full_name = value

    @property
    def component_prefix(self):
        """Get the component prefix."""
        return self._component_prefix

    @component_prefix.setter
    def component_prefix(self, value):
        """Set the component prefix."""
        self._component_prefix = value

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self._project_key} - {self._project_name} - {self._project_initials} - " \
               f"{self._project_full_name} - {self._component_prefix}"
