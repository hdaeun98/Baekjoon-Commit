a = input()
a = int(a)
b = input()
b = int(b)
alist = [int(i) for i in str(a)]
blist = [int(i) for i in str(b)]
val1 = a*blist[2]
val2 = a*blist[1]
val3 = a*blist[0]
val4 = a*b
print(str(val1)+"\n"+str(val2)+"\n"+str(val3)+"\n"+str(val4))