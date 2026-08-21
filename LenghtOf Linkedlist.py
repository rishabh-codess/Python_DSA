from commonLL import Node,take_input_better,print_LL

def lenghtofLLLL(head):
    temp=head
    ans=0

    while(temp!=None):
        temp=temp.next
        ans=ans+1
    return ans
headOfLL=take_input_better()
length= lenghtofLLLL(headOfLL)
print (length)
