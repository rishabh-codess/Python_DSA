def QuickSort(arr, low, high):
    if low<high:
        pivot = partition(arr ,low, high)
        QuickSort (arr, low, pivot-1)
        QuickSort(arr, pivot+1, high)

def partition (arr, low, high):
    p=arr[low]
    i = low+1
    j = high 
    while True:
        while i<=j and arr[i]<=p:
            i+=1
            if i<=j:
                arr[i], arr [j]= arr[j], arr[i]
            else:
                break 
    arr[low], arr[j]= arr[j], arr[low]
    return j

arr =[5, 8, 9, 1, 3, 4]
QuickSort (arr, 0, len (arr)-1)
print (arr)