# domain/services/data_processing_service.py
from application.project_service import ProjectService
import pandas as pd

class DataProcessingService:
    def __init__(self):
        """Initialize the DataProcessingService with a ProjectService instance."""
        self.project_service = ProjectService('data/config/project.json')

    def process_data(self, df):
        """
        Process the DataFrame to add 'Estimated' field and convert estimates to hours.

        Args:
            df (pd.DataFrame): The input DataFrame to process.

        Returns:
            pd.DataFrame: The processed DataFrame.
        """
        df['Assignee'] = df['Assignee'].fillna('Unassigned')
        df['Original Estimate'] = df['Original Estimate'].fillna(0)
        df['Remaining Estimate'] = df['Remaining Estimate'].fillna(0)
        df['Estimated'] = df['Original Estimate'].apply(lambda x: 'Yes' if x > 0 else 'No')
        df['Original Estimate'] = df['Original Estimate'] / 3600
        df['Remaining Estimate'] = df['Remaining Estimate'] / 3600
        return df

    def prepare_components_list(self, df):
        """
        Prepare a list of unique components that start with the project key value.

        Args:
            df (pd.DataFrame): The input DataFrame containing project data.

        Returns:
            str: A formatted string of unique components.
        """
        components = set()

        for _, row in df.dropna(subset=['Component/s', 'Project key']).iterrows():
            project_key = str(row['Project key']).strip()
            project_prefix = self.project_service.get_component_prefix(project_key)

            if project_prefix is None:
                continue  # Skip if project prefix is not found

            for comp in str(row['Component/s']).split(', '):
                if comp.startswith(project_prefix):
                    components.add(comp)

        sorted_components = sorted(components)
        return sorted_components  # Return a sorted list of components
