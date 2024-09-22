nm=[int(x) for x in input().split()]
n=nm[0]
m=nm[1]
a=[0]*m
for i in range(n):
    l=[int(x) for x in input().split()]
    n1=l[0]
    for i in range(n1):
        a[l[i+1]-1]=1
if 0 in a:
    print('NO')
else:
    print('YES')
