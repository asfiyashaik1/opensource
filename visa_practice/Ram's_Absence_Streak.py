n=int(input())
arr=list(map(int,input().split()))
curr=0
max_z=0
for i in range(n):
    if arr[i]==0:
        curr+=1
    else:
        curr=0
    if curr>max_z:
        max_z=curr
    
print(max_z)
        
