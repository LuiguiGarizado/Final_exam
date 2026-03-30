from add import add_student
from functions import *
from  Files import save_csv

students= []
# the heart of the code"
def main(students):
    keep_running = True
    # while it true, it will display the menu constantly
    while keep_running:
        try:
            print("\n" + "-"*50)
            print("CORE MENU")
            print("-"*50)
            print("1. Add students")
            print("2. Show students")
            print("3. search students")
            print("4. update students")
            print("5. delete students")
            print("6. save csv")
            print("7. Exit")
            print("="*50)
            # ask the user to choose one option
            option = input("Choose an option (1-9): ").strip()
            
            if option == "1":
                add_student(students)
            elif option == "2":
                show_student(students)
            elif option == "3":
                # search student by name 
                name = input("student name to search: ")
                coders = search_student(students, name)
                if coders: # verify if the student exist
                    print(f"Found: {coders}")
                else:
                    print("student not found")
            elif option == "4":
                name = input(" student name to search: ")
                course= input("New course (Enter to skip): ")
                status= input("New status (Enter to skip): ")
                update_student(students, name, course, status)
            elif option == "5":
                # delete student by name 
                name = input("student name to delete: ")
                delete_student(students, name)
            elif option == "6":
                save_csv(students)
            elif option == "7":
                print("Thank you for using my Inventory System!")
                keep_running = False
            else:
                print("Invalid option. Please choose 1-6")
        # verify error with the keyboardInterruptor
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            keep_running = False
        # verify if there's any other error
        except Exception as error: 
            print(f" Error: {error}. Returning to menu...")
            # the system won't stop, returning to the main menu 

# it's only to run the program 
if __name__ == "__main__":
    main(students)