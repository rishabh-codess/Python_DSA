step=1

def TowerofHennoi(n,source,destination,auxilary):
    global step
    if (n==0):
        return
    if(n==1):
        print (source,'-->',destination)
        return
    TowerofHennoi(n-1, source, auxilary, destination)
    print (step, 'source','-->', destination)
    step+=1
    TowerofHennoi(n-1, auxilary,destination,source )

n=4
TowerofHennoi(n,'source', 'destination', 'auxilary')