'''
each question 10 test cases
x points for all so question
10 test cases---------->x points
1 test case---------->x/10 points
score will be x/10*no of test cases he passed

'''

t=int(input())
for _ in range(t):
    tot_points,test=map(int,input().split())
    score=(tot_points/10)*test
    print(int(score))
    
