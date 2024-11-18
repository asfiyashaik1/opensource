s=input()
r=''
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        r+=s[i-1]
        r+=str(c)
        c=1
if s:
    r+=s[-1]
    r+=str(c)
print(r)

  
    
