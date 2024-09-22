n=int(input())
if n%4==0 and n%100!=0:
    print('Y')
elif n%100==0:
    if n%400==0 and n%3200!=0:
        print('Y')
    else:
        print('N')
else:
    print('N')
