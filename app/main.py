import sys
import app.utils.connection_manager as cm
import app.utils.parser as parser

session = cm.getSession()


def begin_visualizer():
    print("Starting Fitness Visualizer...")
    workouts = parser.read_workouts()
    print("Workouts successfully loaded.")

def configure_user():
    print("Configuring User Preferences...")
    # Add code to configure user preferences here

    
def close_visualizer():
    print("Exiting Fitness Visualizer...")
    sys.exit()
    
def main():
    print("Welcome to Fitness Visualizer!")
    valid_input = False
    while not valid_input:
        choice = input("1. Open Visualizer Module\n2. User Preferences\n3. Exit\n")
        if choice == "1":
            # Open Visualizer Module
            valid_input = True
            begin_visualizer()
        elif choice == "2":
            # User Preferences
            valid_input = True
            configure_user()
        elif choice == "3":
            # Exit
            valid_input = True
            close_visualizer()
        else:
            print("Invalid input. Please try again.")
    

if __name__ == "__main__":
    main()


