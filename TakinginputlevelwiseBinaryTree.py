from BinaryTreenode import *
from collections import deque

def TakeInputlvlwise():
    data= int(input("enter the data for the root node:"))
    if (data ==-1):
        return None
    root=BinaryTreeNode(data)
    queue=deque({root})

    while len(queue)!=0:
        currentnode=queue.popleft()

        leftchilddata=int(input(f"enter the left child for {currentnode.data}"))

        if (leftchilddata!=1):
            leftnode=BinaryTreeNode(leftchilddata)
            currentnode.left=leftnode
            queue.append(leftnode)

        rightchilddata=int(input(f"enter the right child for {currentnode.data}"))
        if (leftchilddata!=1):
            rightnode=BinaryTreeNode(leftchilddata)
            currentnode.right=rightnode
            queue.append(rightnode)

    return root

print("enter the binary tree data (-1 for no node)")
root = takeinputbinarytree()
printBinaryTree(root)

