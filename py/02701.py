while True:
    try:
        a=[int(x) for x in input().split()]
    except:
        break
    for i in range(a[0],0,-1):
        if a[0]%i==0 and a[1]%i==0:
            print(i)
            break


