n=int(input())
arr=list(map(int,input().split()))
'''
way1
flag=0
for i in range(1,n):
    if arr[i]<arr[i-1]:
        flag=1
if flag==0:
    print("true")
else:
    print("false")
  '''
#way2
sort=sorted(arr)
if arr==sort:
    print("true")
else:
    print("false")
    
