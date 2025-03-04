# application/extractor_controller.py

from application.extractor_service import ExtractorService
from application.csv_service import CSVService
from application.file_management_service import get_user_file_selection
import os

def main():
    input_folder = "data/input/raw"
    output_folder = "data/input/massaged"

    csv_service = CSVService()
    extractor_service = ExtractorService(csv_service)

    files = extractor_service.list_files(input_folder)
    if not files:
        print("No files found in input folder.")
        return

    selected_files = get_user_file_selection(files)
    if selected_files:
        extractor_service.process_files(input_folder, output_folder, selected_files)

if __name__ == "__main__":
    main()
