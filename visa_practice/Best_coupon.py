#hackerrank question -03
bill=int(input())
c1=int(bill-((10/100)*bill))
c2=bill-100
print(min(c1,c2))
