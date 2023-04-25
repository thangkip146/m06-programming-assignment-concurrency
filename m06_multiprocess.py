import multiprocessing
from datetime import datetime
import time
import random

def print_time():
    now = datetime.now()
    # waiting randome number of seconds
    time.sleep(random.random())
    # print current time 
    print("Today's date and time is P{}".format(now))

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=print_time())
    process2 = multiprocessing.Process(target=print_time())
    process3 = multiprocessing.Process(target=print_time())
    
    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    print("Done")
