s=input()
ans=''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        ans=ans+chr(ord(i)-32)
    elif ord(i)>=65 and ord(i)<=90:
        ans=ans+chr(ord(i)+32)
    else:
        ans=ans+i
print(ans)