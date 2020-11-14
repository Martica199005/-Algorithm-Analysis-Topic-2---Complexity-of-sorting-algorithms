import lists
import time


# Function insertion sort 
def insertionsort(l): 
  
    # Consider the element l[0] already ordered 
    for i in range(1, len(l)): 
  
        current = l[i] 
  
        # Move elements of l, that are > current, to one position ahead of their current position 
        j = i-1
        while j >=0 and current < l[j] : 
                l[j+1] = l[j] 
                j -= 1
        l[j+1] = current 
    return l




# Function mergesort 
def mergesort(l): 
    if len(l) >1: 
        middle = len(l)//2 # Finding the middle of the array 
        L = l[:middle] # first half  
        R = l[middle:] # second half 
  
        mergesort(L) # Sorting the first half 
        mergesort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Sorting data 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                l[k] = L[i] 
                i+= 1
            else: 
                l[k] = R[j] 
                j+= 1
            k+= 1
          

        while i < len(L): 
            l[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            l[k] = R[j] 
            j+= 1
            k+= 1
    return l




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
