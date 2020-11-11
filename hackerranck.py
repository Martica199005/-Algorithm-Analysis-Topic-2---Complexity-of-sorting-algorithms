import math
import os
import random
import re
import sys

#
# Complete the 'insertionsort' function below.
#
# The function accepts INTEGER_ARRAY l as parameter.
#

def insertionsort(arr):
    # Write your code here
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

if __name__ == '__main__':

    l = list(map(int, input().rstrip().split()))

    insertionsort(l)

    print(' '.join(map(str, l)))



#2 function

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mergesort' function below.
#
# The function accepts INTEGER_ARRAY l as parameter.
#

def mergesort(arr):

    # Write your code here
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        
        mergesort(L) # Sorting the first half 
        mergesort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
        



if __name__ == '__main__':

    l = list(map(int, input().rstrip().split()))

    mergesort(l)

    print(' '.join(map(str, l)))
