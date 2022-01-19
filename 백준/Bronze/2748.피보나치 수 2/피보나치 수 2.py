n=int(input())
f=[]
for i in range(n+1):
    if i==0:
        s=0
    elif i<=2:
        s=1
    else:
        s=f[-1]+f[-2]
    f.append(s)    
print(f[-1])