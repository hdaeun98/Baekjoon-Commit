import sys

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    print(x+y)