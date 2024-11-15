'''
1hr---60mins
24hr(1-day)---1440mins
zdays---?
?=(1440*z)/1
'''
x,y,z=map(int,input().split())
time=x*y
days=(1440*z)
if time<=days:
    print("YES")
else:
    print("NO")
