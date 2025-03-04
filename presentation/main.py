# presentation/main.py

from application.analyzer_controller import main as analyzer_main
from application.cleaner_controller import main as cleaner_main
from application.extractor_controller import main as extractor_main

def run_analyzer():
    analyzer_main()

def run_cleaner():
    cleaner_main()

def run_extractor():
    # Assuming you have an extractor controller in the application layer
    extractor_main()

def main():
    while True:
        print("\nC. Clean data")
        print("A. Analyze data")
        print("E. Extract data")
        print("X. Exit application")

        user_input = input("Please enter the process you need: ").strip().lower()

        if user_input == 'x':
            print("Exiting application.")
            exit()
        elif user_input == 'c':
            run_cleaner()
        elif user_input == 'a':
            run_analyzer()
        elif user_input == 'e':
            run_extractor()
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
