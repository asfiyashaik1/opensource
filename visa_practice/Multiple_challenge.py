n=int(input())
'''
this is give O(n) of time complexity that is why our test cases are not passing
we can do something with the lcm of them both
c=0
for i in range(3,n+1):
    if i%5==0 or i%3==0 or(i%5==0 and i%3==0):
        c=c+1
print(c)
'''
c1=(n)//3
c2=(n)//5
c3=(n)//15
c=c1+c2-c3
print(c)
