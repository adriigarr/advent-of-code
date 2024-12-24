"""
 The locations are listed by location ID.
Figure out how often each number from the left list appears on the right list.
 1. Calculate how many times the number of the left appears in the list of the right
 2. Calculate the similarity score (value of number * number of appearances)
 3. Return Total similarity value
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

num_appearances = 0
similarity_score = 0
list3 = []
for i in list1:
    for j in list2:
        if i == j:
            num_appearances += 1
    similarity_score = i * num_appearances
    list3.append(similarity_score)
    num_appearances = 0

total_similarity_score = 0
for i in range(len(list3)):
    total_similarity_score += list3[i]

print(total_similarity_score)