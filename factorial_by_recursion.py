def factorial(n):
    smallAns= factorialfour(n-1)
    ans = n*smallAns
    return ans 

def factorialfour(n):
    smallAns= factorialthree (n-1)
    ans = n*smallAns
    return ans 

def factorialthree(n):
    smallAns= factorialtwo(n-1)
    ans = n*smallAns
    return ans 

def factorialtwo(n):
    smallAns= factorialone(n-1)
    ans = n*smallAns
    return ans

def factorialone (n):
    return 1
 
print(factorial(5))
 ## using recursion 
def factorial(n):
    if(n==1):
        return 1
    smallAns= factorial (n-1)
    ans = n*smallAns
    return ans
    

print(factorial(7))