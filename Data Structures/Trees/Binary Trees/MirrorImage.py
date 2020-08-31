n,q=map(int,input().split())
class Node():
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right= None
     
def check(left,right,n1):
    if left==None or right==None:
        return -1
    if left==n1:
        return right
    if right==n1:
        return left
    result=check(left.left,right.right,n1)
    if result!=-1:
        return result
    return check(left.right,right.left,n1)
 
 
l=[Node(i) for i in range(1,n+1)]
for i in range(n-1):
    r,p,s=input().split()
    r,p=int(r),int(p)
    root=l[r-1]
    child=l[p-1]
    if s=="R":
        root.right=child
    if s=="L":
        root.left=child
for i in range(q):
    n1=int(input())
    if l[0]==l[n1-1]:
        print(l[0].data)
    else:
            final=check(l[0].left,l[0].right,l[n1-1])
            if final!=-1:
                print(final.data)
            else:
                print(-1)
