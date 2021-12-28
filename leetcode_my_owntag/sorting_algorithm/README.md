# 1 Selection sort 

time complexity O(n^2) space complexity O(1)

    #Python program for implementation of Selection
    #Sort
    import sys
    A = [64, 25, 12, 22, 11]
 
    # Traverse through all array elements
    for i in range(len(A)):
     
      # Find the minimum element in remaining
      # unsorted array
      min_idx = i
      for j in range(i+1, len(A)):
          if A[min_idx] > A[j]:
              min_idx = j
             
      # Swap the found minimum element with
      # the first element       
      A[i], A[min_idx] = A[min_idx], A[i]
 
    # Driver code to test above
    print ("Sorted array")
    for i in range(len(A)):
        print("%d" %A[i]),
        
        
   # 2. Bubble sort 
   
   time complexity O(n^2), space complexity O(1)
    
    # Python program for implementation of Bubble Sort
 
    def bubbleSort(arr):
        n = len(arr)
 
        # Traverse through all array elements
        for i in range(n):
 
            # Last i elements are already in place
            for j in range(0, n-i-1):
 
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
 
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]
 
    bubbleSort(arr)
 
    print ("Sorted array is:")
    for i in range(len(arr)):
        print ("%d" %arr[i]),


# 3. Insertion sort 
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm 

To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

    def insertionSort(arr):
 
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
 
            key = arr[i]
 
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
 
 
    # Driver code to test above
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    for i in range(len(arr)):
        print ("% d" % arr[i])
