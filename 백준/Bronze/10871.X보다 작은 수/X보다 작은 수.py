n,x=map(int, input().split())
s=''
a=list(map(int, input().split()))
for i in range(n):
    if a[i]<x:
        s+=(str(a[i])+' ')
print(s)