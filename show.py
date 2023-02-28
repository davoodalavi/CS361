import time
import random

if __name__ == '__main__':

    while True:
        time.sleep(1)
        file = open('Movie.txt', 'r+')
        l = file.readline()
        file.close()

        if len(l) != 0:
            file = open('Movie.txt','w')
            file.truncate(0)
            file.seek(0)

            file.write(f"{random.randint(0,3)}")
            file.close()


