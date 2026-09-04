class Node:
    def __init__(self, data):
        self.data= data
        self.Next=None

class StackUsingLL:
    def __init__(self):
        self.head= None
        self.size=0

    def Push(self, data):
        NewNode=Node(data)
        self.size+=1 #very imp
        if(self.head==None):
            self.head= NewNode
            return f"added{data} to the stack"

        NewNode.Next=self.head
        self.head=NewNode
        return f"added{data} to the stack"
    def Top(self):
        if self.head is None:
            return "no top element is present"

        return self.head.data

    def Pop(self):

        if self.head is None: 
            return "no top element is present"
        dataAttop=self.head.data
        self.head=self.head.Next
        self.size-=1
        return dataAttop

    def Size(self):
        return self.size

    def IsEmpty(self):
        return self.size==0

mystack=StackUsingLL()

print(mystack.IsEmpty())
print(mystack.Push(10))
print(mystack.Push(20))
print(mystack.Push(30))
print(mystack.Push(40))
print(mystack.IsEmpty())
print(mystack.Pop())
print(mystack.Pop())
print(mystack.Size())
print(mystack.Top())
