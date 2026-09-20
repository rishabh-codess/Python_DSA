from commons import TreeNode,printtreedetailed
from collections import deque

def Takeinputlvlwise():
    data =int(input("enter the root data"))
    root=TreeNode(data)

    queue=deque([root])

    while (len(queue))!=0:
        currentnode= queue.popleft()

        numchildren= int(input("enter the number of children for :"+ str(currentnode.data)))
        for i in range (numchildren):
            childata=int(input(f"enter the data for {i+1} child of {currentnode.data}:"))
            childnode=TreeNode(childata)
            currentnode.children.append(childnode)
            queue.append(childnode)
    return root
root =Takeinputlvlwise()
printtreedetailed(root)

