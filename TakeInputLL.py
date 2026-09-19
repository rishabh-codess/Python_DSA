
class Node:
    def __init__(self, value ):
        self.data = value
        self.next = None

first =Node(1)
second =Node(2)
third = Node(3)

print(id(first),(second),(third))

first.next= second
second.next= third

head =first

del(first)
del(second)
del(third)

def printLL(head):
    while(head!=None):
        print(head.data)
        head =head.next
    return

printLL(head)


def TAkeINput():
    value=int(input("enter the value of node:- "))
    head = None
    while (value!=-1):
        NewNode=Node(value)
        if(head==None):
            head=NewNode
        else:
            head.next=NewNode

        value=int(input("enter the value of node:- "))
    return head
newhead=TAkeINput()
printLL(newhead)