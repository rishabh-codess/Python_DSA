def pre_ordertraversal(root):
    if (root is None):
        return
    print(root.data,end="")
    pre_ordertraversal(root.left)
    pre_ordertraversal(root.right)
    print(root.data,end=" ")

def post_ordertraversal(root):
    if (root is None):
        return
    print(root.data,end="")
    post_ordertraversal(root.left)
    post_ordertraversal(root.right)
    print(root.data,end=" ")

post_ordertraversal(root1)