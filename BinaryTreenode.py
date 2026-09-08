class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=BinaryTreeNode(1)
root.left=BinaryTreeNode(2)
root.right=BinaryTreeNode(3)

def printBinaryTree(root):

    print (root.data)

    print (root.left)
    print (root.right)
    
