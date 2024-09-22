n=int(input())
l=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in range(n):
    s=[int(x) for x in input()]
    year=s[0]*1000+s[1]*100+s[2]*10+s[3]
    m=s[4]*10+s[5]
    d=s[6]*10+s[7]
    if m<=2:
        year-=1
        m+=12
    c=year//100
    y=year%100
    w=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1)
    print(l[w%7])

