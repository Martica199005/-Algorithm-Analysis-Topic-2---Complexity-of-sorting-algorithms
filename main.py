import lists
import time


# Function to do insertion sort 
def insertionsort(l): 
  
    # Traverse through 1 to len(l) 
    for i in range(1, len(l)): 
  
        key = l[i] 
  
        # Move elements of l[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < l[j] : 
                l[j+1] = l[j] 
                j -= 1
        l[j+1] = key 
    return l




# Python program for implementation of MergeSort 
def mergesort(l): 
    if len(l) >1: 
        mid = len(l)//2 # Finding the mid of the array 
        L = l[:mid] # Dividing the array elements  
        R = l[mid:] # into 2 halves 
  
        mergesort(L) # Sorting the first half 
        mergesort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                l[k] = L[i] 
                i+= 1
            else: 
                l[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            l[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            l[k] = R[j] 
            j+= 1
            k+= 1
    return l



#3 exercise
# Find computation time for sorting algorithms and create files insertionsort.out and mergesort.out.


def write_out(filename,word):
  # The 'a' flag tells Python to keep the file contents
  # and append (add line) at the end of the file.
  myfile = open(filename, 'a')

  # Add the line
  myfile.write(word+"\n")

  # Close the file
  myfile.close()



new_list=lists.lists
for i in new_list:

  t = time.process_time()
  sorted=insertionsort(i)
  elapsed_time = time.process_time() - t
  #time in seconds
  #len(i) is the size of the given array and also the x for the plot
  word=str(len(i))+" "+str(elapsed_time)
  print(word)
  write_out('output/insertionsort.out',word)

print('\t')

for i in new_list:
  t1= time.process_time()
  merged=mergesort(i)
  elapsed_time1 = time.process_time() - t1
  #time in seconds
  word1=str(len(i))+" "+str(elapsed_time1)
  print(word1)
  write_out('output/mergesort.out',word1)