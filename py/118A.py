s=list(input().lower())
i=0
while i < len(s):
    if s[i]=='a' or s[i]=='o' or s[i]=='u' or s[i]=='e' or s[i]=='y' or s[i]=='i':
        s.pop(i)
    else:
        i+=1
ans='.'.join(s)
print('.'+ans)




