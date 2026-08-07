def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

# Example Usage
unsorted_list = [12, 25, 11, 34, 90, 22]
sorted_list = selection_sort(unsorted_list)
print("Sorted Elements :", sorted_list)