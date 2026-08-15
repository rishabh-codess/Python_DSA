def Return_subsquence(s1):
    if (s1==''):
        ans=['']
        return ans 

    SmallAns=Return_subsquence(s1[1:])
    mychar=s1[0]
    ans=[]
    ans.extend(SmallAns)

    for eachpermutation in SmallAns:
        ans.append(mychar + eachpermutation)

    return ans 

s1='abcd'
l1=Return_subsquence(s1)
print (l1)
    
