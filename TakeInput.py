from commons import TreeNode, printtreedetailed
def Takeinput():
    data =int(input("enter the data for the node"))
    node =TreeNode(data)

    numChild=int(input(f"enter the number of children for {data} :"))

    for _ in range (numChild):
        child =Takeinput()
        node.children.append(child)
    return node

root= Takeinput()
printtreedetailed(root)


