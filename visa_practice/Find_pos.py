n,x=map(int,input().split())
arr=list(map(int,input().split()))
if x in arr:
    ind=arr.index(x)
    print(ind)
else:
    arr.append(x)
    arr.sort()
    ind=arr.index(x)
    print(ind)
