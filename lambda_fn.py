# def addition(a,b):
#     return a+b 
# print  (addition(22,8))

# squareroot= lambda num:num**0.5
# print(squareroot(25)) 

nums=list(map(int,input("enter the numbers: ").split()))
squared=list(map(lambda x:x**2, nums))
print(squared)
