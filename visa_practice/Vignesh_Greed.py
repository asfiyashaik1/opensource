n=int(input())
arr=list(map(int,input().split()))
'''
to determine that we can form a triangle or not we need to check if 
adding of two side will be greater than the length of the 3rd side
'''
curr_per=0
max_per=0
form='false'
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j] and arr[j]+arr[k]>arr[i]:
                form='true'
                curr_per=arr[i]+arr[j]+arr[k]
                if curr_per>max_per:
                    max_per=curr_per
                    curr_per=0
if form=='true':
    print(max_per)
else:
    print(-1)
                

        
    
