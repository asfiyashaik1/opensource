n=int(input())
arr=list(map(int,input().split()))
'''
way 1---- using set opeartion but we may not get it in same order as it appears
print(*set(arr))
'''
#way2
ans=[]
for i in arr:
    if i not in ans:
        ans.append(i)
print(*ans)
