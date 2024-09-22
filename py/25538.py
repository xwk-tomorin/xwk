n=int(input())
n2=bin(n)[2:]
n3=n2[::-1]
print(['No','Yes'][n2==n3])
