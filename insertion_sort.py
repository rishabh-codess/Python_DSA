def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        key = arr[i]
        j= i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
    return arr 


unsorted_list = [12, 25, 11, 34, 90, 22]
sorted_list = insertion_sort(unsorted_list)
print ("sorted list is :", sorted_list)