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

def PrintTree(Root):
    print(Root.data)

    for eachChild in Root.children:
        PrintTree(eachChild)

PrintTree(Root)

def printtreedetailed(Root):
    if (Root==None):
        return
    print (f"{Root.data}:", end="")

    for eachChild in Root.children:
        print (eachChild.data,end=",")
    print()

    for eachChild in Root.children:
        printtreedetailed(eachChild)
printtreedetailed(Root)

