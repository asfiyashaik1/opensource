n=int(input())
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
keys=list(freq.keys())
vals=list(freq.values())
pos=vals.index(1)
print(keys[pos])
