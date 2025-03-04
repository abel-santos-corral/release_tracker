import os
import pandas as pd
from application.project_service import ProjectService

class CSVService:
    def __init__(self):
        self.columns_needed = [
            "Summary",
            "Issue key",
            "Issue Type",
            "Status",
            "Assignee",
            "Original Estimate",
            "Remaining Estimate",
            "Component/s",
            "Fix Version/s",
            "Project key",
            "Project name"
        ]
        self.project_service = ProjectService('data/config/project.json')

    def load_csv(self, file_path):
        """Load the CSV file into a DataFrame."""
        return pd.read_csv(file_path, sep=';', encoding='utf-8')

    def filter_columns(self, df):
        """Filter the DataFrame to include only the needed columns."""
        return df[self.columns_needed].copy()

    def process_components(self, df):
        """Process the 'Component/s' column to retain only relevant components."""
        # Retrieve the project mapping from the ProjectService
        project_mapping = self.project_service.get_project_mapping()
        df["Component/s"] = df.apply(
            lambda row: ", ".join([
                c.strip() for c in str(row["Component/s"]).split(",")
                if c.strip().startswith(project_mapping.get(row["Project key"], ""))
            ]) if pd.notna(row["Component/s"]) else "",
            axis=1
        )
        return df


    def process_fix_versions(self, df):
        """Process the 'Fix Version/s' column to retain only the first version."""
        df["Fix Version/s"] = df["Fix Version/s"].apply(
            lambda x: x.split(",")[0].strip() if pd.notna(x) else ""
        )
        return df

    def save_csv(self, df, output_path):
        """Save the DataFrame to a CSV file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, sep=";", index=False, encoding="utf-8")
        print(f"Processed file saved: {output_path}")
