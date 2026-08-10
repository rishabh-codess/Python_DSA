def power2(n):
    if (n==1):
        return 1
    smallAns =power2(n-1)

    ans =2*smallAns

    return ans 

print (power2(8))