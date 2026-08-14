def linearSearchUsingRecursion(l1,x, index):
    if (len(l1)==index):
        return False

    ansFromRecursion= linearSearchUsingRecursion(l1, x, index+1)

    return l1[index]==x or ansFromRecursion
ans= linearSearchUsingRecursion([1,2,3,4,5,6,],2,0)

print(ans)
    