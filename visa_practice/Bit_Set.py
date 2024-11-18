#testcase#2 failing
n=int(input())
k=int(input())
bi=bin(n)
b=bi[2:]
if k<len(b) and b[-k]=='1':
    print("true")
else:
    print("false")
