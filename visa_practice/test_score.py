n,x,y=map(int,input().split())
tot_marks=n*x
if y%x==0 and y<=tot_marks:
    print("YES")
else:
    print("NO")
