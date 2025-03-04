# application/extractor_service.py

import os
from application.csv_service import CSVService

class ExtractorService:
    def __init__(self, csv_service: CSVService):
        self.csv_service = csv_service

    def list_files(self, directory):
        """List files in the given directory."""
        try:
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            return files
        except FileNotFoundError:
            print(f"Error: The directory '{directory}' does not exist.")
            return []

    def process_files(self, input_folder, output_folder, selected_files):
        """Process the selected files."""
        for file in selected_files:
            file_path = os.path.join(input_folder, file)
            df = self.csv_service.load_csv(file_path)
            df = self.csv_service.filter_columns(df)
            df = self.csv_service.process_components(df)
            df = self.csv_service.process_fix_versions(df)
            output_filename = os.path.basename(file_path).replace(".csv", "_massaged.csv")
            output_path = os.path.join(output_folder, output_filename)
            self.csv_service.save_csv(df, output_path)
