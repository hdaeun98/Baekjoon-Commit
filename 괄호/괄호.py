n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
for j in range(n):
    m=[]
    flag=True
    r=l[j]
    for i in range(len(r)):
        if r[i]=='(':
            m.append(r[i])
        else:
            if len(m)==0:
                flag=False
                break;
            else:
                m.pop()
    if len(m)!=0 or flag==False:
        print('NO')
    else:
        print('YES')