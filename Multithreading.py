# Multithreading in python: 
# Multithreading is atechnique in programming that allows Multiple thread of execution to run concurrently within asingle process. In python We can use the threading module to implement Multithreading we will take acloser look at the module and its various functions and how they can be used in python. 
# Importing Threading: 
# We can use threading by importing the threding module 
# Creating threading
import threading 
def my_func():
    print("Hello from thread", threading.current_thread().name)
    thread = threading.Thread(target=my_func)
    thread.start()
    thread.join()

