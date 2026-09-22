class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]

Root=TreeNode(1)
Child1=TreeNode(2)
Child2=TreeNode(3)
Child3=TreeNode(4)

Root.children.append(Child1)
Root.children.append(Child2)
Root.children.append(Child3)
