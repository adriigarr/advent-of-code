"""
 The locations are listed by location ID.
 Two lists -> have to be reconcile
 1. organise the list: smallest number on the right list next to the smallest number on the left list
 2. how far apart the two numbers are -> and add up all of the distance (be careful because the distance has to be always positive)
 3. return the total distance -> 
"""
import pandas as pd
df = pd.read_fwf("2024/day01/input.txt", header=None, delim_whitespace=True)

# # the list has two columns and we want to save each column to a different list
list1= []
list2=[]

list1 = list(df.iloc[:,0])
list2 = list(df.iloc[:,1])


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            

mergeSort(list1)
mergeSort(list2)

list3 = []
for i in range(len(list1)):
    if(list1[i] > list2[i]):
        list3.append(list1[i] - list2[i])
    else:
        list3.append(list2[i] - list1[i])

sum_total = 0
for i in range(len(list3)):
    sum_total += list3[i]

print(sum_total)