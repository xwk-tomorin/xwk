n1,m1=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n1)]
n2,m2=map(int,input().split())
B=[list(map(int,input().split())) for i in range(n2)]
n3,m3=map(int,input().split())
C=[list(map(int,input().split())) for i in range(n3)]
if m1==n2 and n1==n3 and m2==m3:
    for i in range(n1):
        for j in range(m2):
            ans=0
            for k in range(m1):
                ans+=A[i][k]*B[k][j]
            ans+=C[i][j]
            if j!=m2-1: print(ans,end=' ')
            else:print(ans)
else:
    print('Error!')