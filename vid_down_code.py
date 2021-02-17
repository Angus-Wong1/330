def Merge(L, R, arr):
    
    n1 = len(L)
    n2 = len(R)
    
    i, j = 0, 0
    
    while i < n1 and j < n2: 
        if L[i] < R[j]: 
            arr.append(L[i])
            i += 1
        else:
            arr.append(R[j]) 
            j += 1
    
    arr = arr + L[i:] + R[j:]
    
    return arr

# Python program for implementation of MergeSort
def MergeSort(array):
    if len(array) > 1:
 
         # Finding the mid of the array
        mid = len(array)//2
 
        # Dividing the array elements
        L = array[:mid]
 
        # into 2 halves
        R = array[mid:]
 
        # Sorting the first half
        MergeSort(L)
 
        # Sorting the second half
        MergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    
    return array

def inversionCount_MergeSort(array):
    
    n = len(array)
    inv_count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if array[i] > array[j]: 
                inv_count += 1
  
    return inv_count 