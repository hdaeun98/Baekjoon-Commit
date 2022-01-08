n=int(input())
c=0
on=n
m=n
while True:
    c+=1
    m=n%10
    n=int(n/10)
    n=n+m
    n=(m%10)*10+(n%10)
    if n==on:
        break
print(c)