#threading is a technique where a program can run multiple operations (tasks)concurrently (at the same time) using threads.
# a thread is the smallest unit of a program that can be excuted independently
# a thread shares the same memory space as other threads in the same process

import time
def squares(numbers):
    print(f"squares of numbers")
    for i in numbers:
        time.sleep(0.2)  
        print(f"squares {i**2}")
initial_time = time.time()        
list_1 = [1,2,3,4,5] 
squares(list_1)
print(f"time taken{time.time()-initial_time}")  



def cubes(numbers):
    print(f"cubes of numbers")
    for i in numbers:
        time.sleep(0.2)
        print(f"cubes {i**3}")
initial_time = time.time()        
list_1 = [1,2,3,4,5] 
cubes(list_1) 
print(f"time taken{time.time()-initial_time}") 


import threading
import time
def square(numbers):
    print(f"square of numbers: ")
    for i in numbers:
        time.sleep(0.2) 
        print(f"squares: {i**2}")

def cubes(numbers):
    print(f"cubes of numbers:")
    for i in numbers:
        time.sleep(0.2)
        print(f"cubes: {i**3}")
initial_time = time.time()
list_1 = [1,2,3,4,5]        
t1 = threading.Thread(target=square,args=(list_1,))
t2 = threading.Thread(target=cubes,args=(list_1,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"time taken{time.time()-initial_time}")