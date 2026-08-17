def MergeSort(arr):
    if len(arr)<=1:
        return arr
    
    m =len(arr)//2
    l_half= arr[:m]
    r_half=arr[m:]

    l_half= MergeSort (l_half)
    r_half= MergeSort(r_half)
    return Merge(l_half,r_half)

def Merge(left, right):
    new=[]
    i, j = 0, 0
    while i<len (left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append (right[j])
            j+=1

    new.extend(left[i:])
    new.extend(right[j:])
    return new 


print (MergeSort([10, 5, 70, 100, 80]))    
    