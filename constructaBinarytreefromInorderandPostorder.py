def construct_tree_from_inorder_and_Postorder(inorder,postorder,ins,ine,pos,poe):
    if (ins>ine or pos>poe):
        return None
    root_data=postorder[poe]

    root=Treenode(root_data)

    rootIndexInorder=-1

    for i in range(ins,ine+1):
        if (inorder[i]==root_data):
            rootIndexInorder=i
            break

    if (rootIndexInorder==-1):
        print("root not found in inorder, plz check")
        return None
    lins=ins
    line=rootIndexInorder-1
    lpos= pos
    lpoe=pos+(line-lins)

    rins=rootIndexInorder+1
    rine=ine
    rpos=lpoe+1
    rpoe=poe-1

    root.left=construct_tree_from_inorder_and_Postorder(inorder, postorder,lins, line,lpos,lpoe)
    root.right=construct_tree_from_inorder_and_Postorder(inorder, postorder,rins, rine, rpos,rpoe)

    return root 

inorder=[4, 2, 5, 1, 3, 6]
postorder=[4, 5, 2, 6, 3, 1]
n=len(inorder)
root=construct_tree_from_inorder_and_Postorder(inorder, postorder, 0, n-1,0, n-1)


