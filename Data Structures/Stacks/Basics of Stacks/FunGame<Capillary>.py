n = int(input())                                        #First line consists of a number n, size of the list provided.
arr = [int(x) for x in input().split()]                 #Next line consists of n numbers separated by space.
m = len(arr)
i,j = 0,m-1
list = []
while i!=m and j!=-1:
    if arr[i] > arr[j]:
        list.append(1)
        j-=1
    elif arr[i] < arr[j]:
        list.append(2)
        i+=1
    else:
        list.append(0)
        j-=1
        i+=1
for k in list:
    print(k, end=' ')
