import sys
   
def swap(a,b):
    t=a
    a=b
    b=t
    return a,b

def insert(heap, x):
    child = len(heap)
    heap.append(x)
    while True:
        parent=(child)//2
        if heap[child]>heap[parent]:
            heap[parent], heap[child]=swap(heap[parent], heap[child])
            child = parent
        else:
            break
    return heap

def delete(heap, x):
    tmp=heap[1]
    heap[1]=heap[len(heap)-1]
    heap.pop()
    parent=1
    while True:
        child=(parent)*2
        if child+1 < len(heap):
            if heap[child] < heap[child+1]:
                child+=1
        elif child>= len(heap):
            break
        if heap[parent]<heap[child]:
           heap[parent], heap[child]=swap(heap[parent], heap[child])
           parent=child
        else:
            break
    print(tmp)
    return heap


n=int(sys.stdin.readline())
l=[2**31]
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if len(l)==1:
            print(0)
        else:
            delete(l,x)
    else:
        insert(l,x)