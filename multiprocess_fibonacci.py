# coding: utf-8
# In[3]:

# Author : Michel Benites Nascimento
# Descr. : App that triggers some threads, in order to generate a CPU intensive multi threaded process.

import multiprocessing as mp
import sys
import time

# Define function to do some calculates. Parameter : iterations
def FibonacciCalc(pIter):

    # Infinite loop.
    while True:
        
        # Delays 1 second. 
        time.sleep(1)

        # Print name and Id threads.
        print ('Name:', mp.current_process().name, 'ID:', mp.current_process().pid)
        
        # Starts the variables.
        x, y = 1, 1
          
        # Loop to generate the lines in the file.
        for i in range( pIter - 1 ):
            x, y = y, x + y          

    # This return will never be executed.
    return x    
    
# Main function
def main ():
    
    # Verify if the numbers of arguments are Ok.
    if len(sys.argv) < 2:
        print('Invalid number of arguments!!!!')
        return
        
    # Getting the arguments value.
    sThreads = sys.argv[1]
        
    # Converting the arguments into number.
    numThreads = int(sThreads)

    # Defining the number of iterations
    piter = 100000
    
    # Loop to create the files.
    for i in range(numThreads):

        sNameT = 'Thread ' + str(i)

        # Threading the function CreateFile.
        t = mp.Process(name = sNameT, target = FibonacciCalc, args = (piter,))
        
        # Starting the thread
        t.start() 
   
# Calling main function
if __name__ == '__main__':    
    sys.exit(main())

