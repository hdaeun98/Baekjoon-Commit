n=list(range(1,10001))
r=[]
for i in n:
    for j in str(i):
        i+=int(j)
    if i<10001:
        r.append(i)

for k in set(r):
    n.remove(k)
n.sort()
for l in n:
    print(l)