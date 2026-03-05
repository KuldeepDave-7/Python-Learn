# Threading :- Threads are like units of execution. they are assigned to different tasks in a program which
#              allows for the concurrent execution of multiple tasks within a single program.
#              However each thread takes turn running to achieve concurrency 
#              Main thread is incharge for runnning of main body of program   

# GIL :-  (Global interpreter lock) allows only one thread to hold control of python interpreter at a time     

# Multi threading :- Switching between threads, giving the appearance of simultaneous execution.
#                    his makes threading particularly effective for I/O-bound tasks where threads spend time waiting
#                    for external resources (e.g., network requests, disk I/O)

import threading
import time 

#print(threading.active_count())  # Print the count of active thread
#print(threading.enumerate())      # Print all the runnning thread

def writing():
    time.sleep(3)
    print("Writing something")

def listening():
    time.sleep(2)
    print("Listening something")

def talking():
    time.sleep(3)
    print("Saying something")

start = time.perf_counter()

x = threading.Thread(target=writing,args=())
x.start()
y = threading.Thread(target=listening,args=())
y.start()
z = threading.Thread(target=talking,args=())
z.start()

x.join()                  # By doing this the main thread will wait for these threads to complete first
y.join()
z.join()

print(threading.active_count())  
print(threading.enumerate())     
print(time.perf_counter()-start)

# Daemon thread :- Daemon threads are automatically stopped when all non-daemon threads (including the main thread)
#                  have finished their execution. The program does not wait for daemon threads to complete.
#                  used for non-critical, background operations

def timer ():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for ",count, "seconds")

x = threading.Thread(target=timer,daemon=True)
x.start()

answer = input("Waiting for user input: ")
print()

# Multiprocessing :-
from multiprocessing import Process, cpu_count
import time
def include(num):
    count = 0

    while count < num:
        count += 1

start = time.perf_counter()

if __name__ == '__main__':
   x = Process(target=include,args=(50000000,))
   y = Process(target=include,args=(50000000,))

   x.start()
   y.start()
   x.join()
   y.join()

   print(time.perf_counter()-start)
   print(cpu_count())