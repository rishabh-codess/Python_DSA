from commonLL import *

headodd=createLLFromList([1,2,3,4,5])
headeven=createLLFromList([1,2,3,4,5,6])

print_LL(headodd)
print_LL(headeven)

def middleOfLL(head):
    if(head is None or head.next is None):
        return head
    
    length=lengthOfLL(head)
    middle=length//2

    temp= head 
    count=0
    while (count<middle):

        temp=temp.next
        count+=1

    return temp 

def mddleofllwithfastandslow(head):
    if(head is None or head.next is None):
        return head 

    slow =head 
    fast =head 

    while fast is not None and fast.next is not None:
        slow=slow.next
        fast =fast.next.next
        return slow 
    

headOddMid= middleOfLL(headodd)
headevenmid=middleOfLL(headeven)

print(headOddMid.data)
print(headevenmid.data)