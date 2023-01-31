from Ui import *
def main_menu(username):
    while True:
        print('Welcome', username,"!\n")
        print("Please select one of the following options:\nFor optimum experience, please first select your desired price and then your desired destination.\n Changes can be made by returning to the corrisponding menu\n")
        print("1: Set Price\n2: Set Destination\n3:Logout\n")
        choice = input();

        if choice == "1":
            print("Hello!\nThis section allows you to set the dollar amount for plane ticket notification\nPlease enter a number between 50 and 400: ")
            amount = input()
            print("Your notification amount has been set to: ",amount)
            exit

        elif choice == "2":
            print("Hello!\nThis section allows you to set the location you would like to travel to next.\nPlease enter your destination below: \n")
            location = input()
            print("Ok! You will be notified when tickets to ",location,"become available at your desired price!")
            exit
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please select a valid number")




