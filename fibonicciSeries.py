def fibonicci(n):
    if n ==0:
        return 1
    if n == 1:
        return 1
    lastNum= fibonicci(n-1)
    secondlastNum = fibonicci(n-2)
    ans = lastNum + secondlastNum 

    return ans 

print(fibonicci(5))