n=int(input())
l=['I hate']
c='0'

for i in range(n-1):
    if i%2==0:
        c='love'
    else:
        c='hate'
    l.append('that I')
    l.append(c)
l.append('it')
print(' '.join(l))



