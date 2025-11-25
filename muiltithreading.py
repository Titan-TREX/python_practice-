import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

func(2)
func(3)
func(4)

from threading import Thread

def square_numbers():
    for i in range(10):
         i * i

if __name__ == "__main__":
    threads = []
    num_threads = 5

    #create threads

    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)
    # start threads
    for t in threads:
        t.start()
    # wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads have finished execution")      



    # dono parllel 2 kaam kr rhe h ek dusre k sath

import threading
import time

def task1():
    for i in range(5):
        print("Task 1 running...")
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 running...")
        time.sleep(1)

# Threads banana
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Threads start
t1.start()
t2.start()

# Threads wait
t1.join()
t2.join()

print("Done!")
