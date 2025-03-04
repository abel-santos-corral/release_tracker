# application/analyzer_controller.py
import os
from application.csv_service import CSVService
from application.file_management_service import list_files, get_user_file_selection
from domain.services.data_processing_service import DataProcessingService
from domain.services.report_generation_service import ReportGenerationService

def main():
    # Get the root directory of the project
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'release_tracker'))

    input_folder = os.path.join(root_dir, 'data', 'input', 'massaged')
    output_folder = os.path.join(root_dir, 'data', 'output')

    csv_service = CSVService()

    files = list_files(input_folder)
    if not files:
        print("No files found in input folder.")
        return

    selected_files = get_user_file_selection(files)
    if selected_files:
        for file in selected_files:
            file_path = os.path.join(input_folder, file)
            if not os.path.exists(file_path):
                print(f"File {file} not found in the input folder.")
                continue

            df = csv_service.load_csv(file_path)
            df = csv_service.filter_columns(df)
            df = csv_service.process_components(df)
            df = csv_service.process_fix_versions(df)

            # Assuming process_data is a method of DataProcessingService
            data_processing_service = DataProcessingService()
            df = data_processing_service.process_data(df)

            base_filename = os.path.basename(file_path).replace("_massaged", "")
            output_filename = base_filename.replace(".csv", "_report.md")
            output_path = os.path.join(output_folder, output_filename)

            # Assuming generate_report is a method of ReportGenerationService
            report_generation_service = ReportGenerationService()
            report_generation_service.generate_report(df, output_path)

            print(f"Report generated and saved to {output_path}")

if __name__ == "__main__":
    main()
