def CheckBSt(root):
    if root is None:
        return True
    leftMax=findMax(root.left)
    rightMin=findMin(root.right)
    leftBSt=CheckBSt(root.left)
    rightBSt=CheckBSt(root.right)
    ans=leftBSt and rightBSt and (leftMax<root.data)and (root.data<rightMin)
    return ans

root1, root2, root3=createPredefinedBstsmanual()
print (CheckBSt(root3))
root4=BSTNode(5)
root4.left=BSTNode(10)
root4.right=BSTNode(15)
