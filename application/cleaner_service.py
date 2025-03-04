# application/cleaner_service.py

import os

class CleanerService:
    @staticmethod
    def delete_files_in_directory(directory):
        """Delete all files in the specified directory."""
        try:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print(f"All files in '{directory}' have been deleted.")
        except FileNotFoundError:
            print(f"Error: The directory '{directory}' does not exist.")
