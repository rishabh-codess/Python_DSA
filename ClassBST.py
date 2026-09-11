class BsTNoode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def Search (self,data):
        return self.SearchHelper(data,self.root)

    def SearchHelper(self,data,root):

        if (self.root is None):
            return False
        
        if (self.root.data==data):

            return True
        if(data<self.root.data):

            return self.SearchHelper(data,root.left)
        else:
            return self.SearchHelper(data,root.right)


    def Insert(self,data):
        self.root= self.Insert_helper()
    def Insert_helper(self,data,node):

        if(node==None):
            NewNode=BsTNoode(data)
            return NewNode
        
        if (data<node.data):
            node.left=self.Insert_helper(data,node.left)
        else:
            node.right=self.Insert_helper(data,node.right)
            return 

    def delete_helper(self,data,root):
        if (root is None):
            return None
        if(data<root.data):
            root.left=self.delete_helper(data,root.left)

        if(data>root.data):
            root.right=self.delete_helper(data,root.right)

BstObject=BST()

BstObject.Insert(20)
BstObject.Insert(25)
BstObject.Insert(10)
BstObject.Insert(15)
BstObject.Insert(30)

        
        
        