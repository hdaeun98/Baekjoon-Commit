n=int(input())
s=input()
l=s.split()
x=l[0]
u=l[0]
c=0
while c<n-1:
    if int(x)<int(l[c+1]):
        x=l[c+1]
    elif int(u)>int(l[c+1]):
        u=l[c+1]
    c+=1
print(u+" "+x)