def bubble_sort(arr):
    n=len(arr)
    for passes in range(0,n):
        for j in range(0,n-1):
            if (arr[j]> arr[j+1]):
                arr[j], arr[j+1]=arr[j+1], arr [j]
    return arr 

unsorted_list=[11, 12, 3, 17, 40,22]
sorted_list= bubble_sort(unsorted_list)
print (sorted_list) 