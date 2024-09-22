for i in range(int(input())):
    n=int(input())
    ans=n*(n+1)//2
    for i in range(20):
        x=2**i
        if x<=n:
            ans-=2*x
    print(ans)
