class Node:
    def __init__(self, data):
        self.data= data
        self.Next=None

class QueueUsingLL:
    def __init__(self):
        self.head= None
        self.tail=None
        self.len=0

    def Size(self):
        return self.len

    def Isempty(self):
        return self.Size()==0

    def Enqueue(self, data):
        NewNode=Node(data)
        self.len+=1
        if(self.head is None):
            self.head=NewNode
            self.tail=NewNode

        else:
            self.tail.Next=NewNode
            self.tail =NewNode

        return f"added {data} to Queue"

    def Front (self):
        if(self.Isempty()):
            print ("queue is empty")
            return
            
        return self.head.data 

    def dequeue(self):
        if(self.Isempty()):
            print ("queue is already empty")
            return
        
        self.len-=1
        Datatobereturn=self.head.data
        self.head=self.head.Next
        if(self.head==None):
            self.tail=None
        return Datatobereturn


Q =QueueUsingLL()
Q.Enqueue(10)
Q.Enqueue(20)
Q.Enqueue(30)
print(Q.Size())
print(Q.Isempty())
print(Q.Front())
print(Q.dequeue())
print(Q.dequeue())
print(Q.Front())
print(Q.Size())

        
