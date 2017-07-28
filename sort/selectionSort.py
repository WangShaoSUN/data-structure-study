#encoding=utf-8
__author__ = '韶晨'
import random
def min_list(list,start,end):
    min=start
    for i in range(start,end):
        if list[min]>list[i]:
            min=i
    return min
def ssort(list):
    length=len(list)
    for i in range(length):
        min_index=min_list(list,i,length)
        list[i],list[min_index]=list[min_index],list[i]
    return  list
help(random.randint)
x= [random.randint(0,100) for i in range(15)]
print min_list(x,0,15)
# print ssort(x)
print x
print ssort(x)
