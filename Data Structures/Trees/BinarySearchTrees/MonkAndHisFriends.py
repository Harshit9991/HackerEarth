for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(input().split())
    class=set(arr[:n])
    l=[]
    for num in arr[n:]:
        if num in class:
            l.append("YES")
        else:
            l.append("NO")
            class.add(num)
 
    print('\n'.join(l))
