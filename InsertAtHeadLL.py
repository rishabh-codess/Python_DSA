from commonLL import Node,take_input_better,print_LL
head=take_input_better()
print_LL(head)


def InsertAtHead(head,data):
    newnode=Node(data)
    newnode.next =head
    head = newnode
    return head
head=InsertAtHead(head, 1000)
print("after inserting at head: ")
print_LL(head)
 