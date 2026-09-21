def NaturalSum(n):
    if n == 1:
        return 1
    smallaAns= NaturalSum(n-1)
    ans =n + smallaAns 
    return ans 

n =5
print (f"sum of first {n} natural num is" , NaturalSum(n))