n=int(input())
l=[[0]]*n
flag=True
for i in range(n):
    l[i]=[int(x) for x in input().split()]
for j in range(3):
    ans=0
    for i in range(n):
         ans+=l[i][j]
    if ans!=0:
        flag=False
        break
if flag:
    print('YES')
else:
    print('NO')

