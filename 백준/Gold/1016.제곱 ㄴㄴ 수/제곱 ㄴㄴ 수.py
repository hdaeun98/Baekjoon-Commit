import sys
min,max=map(int, sys.stdin.readline().split())
a=[1]*(max+1-min) 
n=2
while n**2<=max:
    #얘는 제곱수 
    i=min//(n**2) #바로 직전 넘버 access
    while i*(n**2)<=max:
        j=i*(n**2)
        if j-min>=0:
            a[j-min]=0
            #max보다 적은 수까지 제곱제곱 0만들기
        i+=1
    n+=1
print(sum(a))