import sys
import heapq

n=int(sys.stdin.readline())
l=[2**31] 
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if len(l)==1:
            print(0)
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l,x)