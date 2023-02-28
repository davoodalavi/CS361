import random
import time

while True:
    if __name__ == '__main__':
        time.sleep(1)
        sfile = open("streamingPlatform.txt","r+")
        sl = sfile.readline()
        sfile.close()

        if not sl:
            continue

        try:
            ints = int(sl)
        except Exception as e:
            pass

        else:
            sfile = open("streamingPlatform.txt", "r+")



