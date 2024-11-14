num=int(input())
s=0
while num!=0:
    rem=num%10
    num=num//10
    s+=rem
if s%2==0:
    print("Vignesh")
else:
    print("Charan")
