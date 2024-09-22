n=int(input())
l=list(map(int,input().split()))
flag=True
for i in range(n-1) :
    if l[i+1]<l[i]:
        flag=False
        break
print(['NO','YES'][flag])