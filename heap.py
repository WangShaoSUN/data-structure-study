#encoding=utf-8
'''
  实现堆算法
'''
def less(x,y):
    return x>y
ll=[2,4,1,3,12]

def heapify(list,i,size,key=less):
    heap=[0]
    heap.append(list)
    while True:
     left=i*2
     right=i*2+1
     m=i
     if  left<=size and key(heap[left],heap[i]):
          m=left
     if  right<=size and key(heap[right],heap[m]):
          m=right
     if m!=i:
          heap[i],heap[m]=heap[m],heap[i]
          i=m
     else:
         break
