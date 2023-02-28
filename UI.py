import time

if __name__ == "__main__":

    while True:
        print("Please enter 1 to look up streaming service of a show or movie. Press 2 to exit")
        selection = input();

        if selection == "1":
            print("Please enter name of show or movie")
            s2 = input()
            file = open("Movie.txt","r+")
            file.write(s2)
            file.close()
            time.sleep(3)
            file = open("Movie.txt", "r+")
            line = file.readline()
            if line == "1":
                print("This show is on Netflix!\n It costs $10.99 for this service")
            elif line == "2":
                print("This show is on Amazon Prime!\n It costs $9.99 for this service")
            elif line == "3":
                print("This show is on Hulu!\n It costs $7.99 for this service ")
            else:
                print("This show is not available for streaming!")
            file.close()

            exit
        elif selection == "2":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid number")


