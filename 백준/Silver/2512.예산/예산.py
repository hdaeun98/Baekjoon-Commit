import sys
n=int(sys.stdin.readline())
b=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
max=max(b)
min=0
while min<=max:
    mid=(min+max)//2
    sum=0
    for i in b:
        if mid<i:
            sum+=mid
        else:
            sum+=i
    if(sum>m):
        max=mid-1
    else:
        min=mid+1
print(max)