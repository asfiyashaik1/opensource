n=int(input())
arr=list(map(int,input().split()))
new=[]
for i in range(1,n):
    new.append(arr[i])
new.append(arr[0])
print(*new)
#way2
n= int(input())
arr = list(map(int, input().split()))

r= arr[1:] + arr[:1]


print(*r)
