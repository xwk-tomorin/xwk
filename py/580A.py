n=int(input())
l=[int(x) for x in input().split()]
ans=0
m=0
for i in range(n-1):
    if l[i]<=l[i+1] :
        m+=1
    else:
        if m+1>ans:
            ans=m+1
        m=0
if m+1>ans:
    ans=m+1
print(ans)
