import sys
k,n=map(int, input().split())
l=[]
for i in range(k):
    a=int(input())
    l.append(a)
s=1
b=max(l)
while s<=b:
    m=(s+b)//2
    c=0
    for i in l:
       c+=i//m
    if c>=n:
        s=m+1
    else:
        b=m-1
print(b)