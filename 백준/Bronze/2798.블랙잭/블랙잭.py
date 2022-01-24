n,m=map(int, input().split())
d=300000
f=0
a=list(map(int, input().split()))
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s=a[k]+a[j]+a[i]
            if m>=s:
                if abs(s-m)<d:
                    d=abs(s-m)
                    f=s
print(f)