from commonLL import *
def ReverseLL(head):
    print_LL (head)

    if(head==None or head.next ==None):
        return head
    
    smalllinkedlisthead=ReverseLL(head.next)

    temp=smalllinkedlisthead

    while(temp.next is not None):
        temp=temp.next
    temp.next=head
    head.next=None

    return smalllinkedlisthead


#reverse linked better 
from commonLL import *
def ReverseLL(head):
    print_LL (head)

    if(head==None or head.next ==None):
        return head
    
    smalllinkedlisthead=ReverseLL(head.next)

    tailofReverseLL=head.next
    tailofReverseLL.next=head
    head.next= None

    return smalllinkedlisthead
