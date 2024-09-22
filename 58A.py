l=[x for x in input()]
inde=[[],[],[],[]]
li=['h','e','l','o']
a=-1
def findit(n,l):
    for i in l:
        if i>n:
            return i
    else:
        return 2000
for i in range(4):
    while li[i] in l:
        c = l.index(li[i])
        inde[i].append(c)
        l[c] = '0'
for i in range(4):
    a=findit(a,inde[i])
    if i==2:
        a=findit(a,inde[i])
    if a==2000:
        print('NO')
        break

else:
    print('YES')


























