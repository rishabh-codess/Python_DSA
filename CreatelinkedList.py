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
