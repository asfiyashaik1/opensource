n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(0,n):
    l=sum(arr[:i])
    r=sum(arr[i+1:])
    a=abs(l-r)
    ans.append(a)
print(*ans)
    
    
