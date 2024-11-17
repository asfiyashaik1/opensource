'''
in an array we have to see which nums are divisble by m and which is not
and then add them seperateley and finally subtract the final numbers
'''
n,m=map(int,input().split())
arr=list(map(int,input().split()))
divm=0
notdivm=0
for i in arr:
    if i%m==0:
        divm+=i
    else:
        notdivm+=i
print(divm-notdivm)
        
