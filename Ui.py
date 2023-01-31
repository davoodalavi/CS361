from main_Menu import *

if __name__ == "__main__":
    while True:
        print("Please select one of the following options:\n")
        print("1:Login\n2:Sign Up\n3:Exit")
        selection = input();

        if selection == "1":
            print("Username: ")
            un = input();
            print("Password: ")
            pw = input();
            main_menu(un)


        elif selection == "2":
            print("This function is coming soon!\n Press 1 to go back\n Press 2 to exit:\n")
            goback = input();
            if goback == "1":
                True
            elif goback == "2":
                exit
            elif selection == "3":
                exit
        elif selection == "3":
            print("Goodbye!")
            break

        else:
            print("Please select a valid number")



