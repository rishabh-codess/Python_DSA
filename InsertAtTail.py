
# from commonLL import Node,take_input_better,print_LL
# def InsertAtTailRecursive(head, data):
#     if (head is None):
#         newnode=Node(data)
#         return newnode
#     head.next =InsertAtTailRecursive(head.next, data)

#     return head 

# head=InsertAtTailRecursive(head, 1000)
# print("after inserting at Tail: ")
# print_LL(head)


class ListNode:
    def __init__(self,val=0, Next=None):
        self.val=val
        self.Next=Next
def AddTwoNum(l1:ListNode, l2:ListNode ,carry:int=0)->ListNode:
    if not l1 and not l2 and carry ==0:
        return None

    val1=l1.val if l1 else 0
    val2= l2.val if l2 else 0
    total=val1+val2+carry 

    node= ListNode(total%10)
    next1=l1.next if l1 else None
    next2=l2.next if l2 else None
    node.next=AddTwoNum(next1,next2, total//10)

    return node

l1=([2,4,3])
l2=([5, 6, 4])
result= AddTwoNum (l1,l2)
print (result)        