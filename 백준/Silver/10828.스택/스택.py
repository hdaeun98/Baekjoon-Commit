import sys
c=int(sys.stdin.readline())
l=[]
for i in range(c):
    t=sys.stdin.readline()
    if "push" in t:
        a=t.split()
        b=int(a[1])
        l.append(int(b)) 
    elif "pop" in t:
        if len(l)==0:
            print("-1")
        else:
            print(l.pop())
    elif "size" in t:
        print(len(l))
    elif "empty" in t:
        if len(l)==0:
            print(1)
        else:
            print(0)
    elif "top" in t:
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])
    c-=1