def linear_search(arr, target):
    size= len(arr)
    for index in range (0, size):
        if (arr[index]==target):
            return index
    return -1

my_list= [10, 20, 30, 40, 70, 60]
target=70
result= linear_search(my_list, target)
print(result)