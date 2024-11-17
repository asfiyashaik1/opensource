'''
x target y runs
total=x-y would be needed but then it will be tie so +1 is also need to make to win 
'''
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    print(x-y+1)
