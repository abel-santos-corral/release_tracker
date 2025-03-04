# application/cleaner_controller.py
import os
from application.cleaner_service import CleanerService

def main():
    raw_folder = "data/input/raw"
    massaged_folder = "data/input/massaged"
    report_folder = "data/output"

    cleaner_service = CleanerService()

    while True:
        print("\nList of Options: ")
        print("A. Clean raw data")
        print("B. Clean massaged data")
        print("C. Clean report data")
        print("D. Clean all data")
        print("\nM. Back to main menu")
        print("X. Exit application\n")

        user_input = input("Please select the option: ").strip().lower()

        if user_input == 'x':
            print("Exiting application.")
            exit()
        elif user_input == 'm':
            os.system("python main.py")
            break
        elif user_input == 'a':
            cleaner_service.delete_files_in_directory(raw_folder)
        elif user_input == 'b':
            cleaner_service.delete_files_in_directory(massaged_folder)
        elif user_input == 'c':
            cleaner_service.delete_files_in_directory(report_folder)
        elif user_input == 'd':
            cleaner_service.delete_files_in_directory(raw_folder)
            cleaner_service.delete_files_in_directory(massaged_folder)
            cleaner_service.delete_files_in_directory(report_folder)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
