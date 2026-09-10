from PredefinedBST import create_predefinedbsts_manual

def Print_BST_in_Range(root, low, high):
    if (root is None):
        return

    if (low< root.data):
        Print_BST_in_Range(root.left,low,high)

    if (root<=root.data<=high):
        print(root.data,end='')

    if (high>root.data):
        Print_BST_in_Range(root.right, low, high)

root1,root2,root3=create_predefinedbsts_manual()
Print_BST_in_Range(root3,25,50)
