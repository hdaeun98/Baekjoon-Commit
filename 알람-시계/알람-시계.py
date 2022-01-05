h,m = input().split()
h = int(h)
m = int(m)
if h != 0:
    t = h*60+m
    newh = int((t-45)/60)
    newm = int((t-45)%60)
    print(str(newh)+" "+str(newm))
else:
    if m>=45:
        newm = m-45
        print(str(h)+" "+str(newm))
    else:
        newh = 23
        newm = abs(m-45)
        m = 60-newm
        print(str(newh)+" "+str(m))