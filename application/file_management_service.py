import os

def list_files(directory):
    """List files in the given directory."""
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        return []

def get_user_file_selection(files):
    """Prompt the user to select a file from the list or process all files."""
    while True:
        print("\nList of Options: ")
        print("A. All files\n")
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")
        print("\nB. Back to main menu")
        print("X. Exit application\n")
        user_input = input("Please select the option: ").strip()

        if user_input.lower() == 'x':
            print("Exiting application.")
            exit()

        if user_input.lower() == 'b':
            os.system("python main.py")
            break

        if user_input.lower() == 'a':
            return files

        if user_input.isdigit():
            file_index = int(user_input) - 1
            if 0 <= file_index < len(files):
                return [files[file_index]]

        print("The file input value is not correct. Please try again.")
