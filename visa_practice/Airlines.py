'''
1 aircraft --- 100 passengers
? aircrafts --- 600 passengers
100x=600
x=600//100
?=n//100
if it is not divisible by 100 we need to round up to the nearest integer
need=?-x
'''
import math
x,n=map(int,input().split())
pas=math.ceil(n/100)
if x>=pas:
    print('0')
else:
    print(abs(pas-x))
