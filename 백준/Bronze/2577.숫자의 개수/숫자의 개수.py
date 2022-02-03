a=int(input())
b=int(input())
c=int(input())
n=str(a*b*c)
for i in range(10):
    c=0
    for j in range(len(n)):
        if(int(n[j])==i):
            c+=1
    print(c)