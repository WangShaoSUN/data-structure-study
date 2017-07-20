import random
def qsort(sorted):
    if sorted==[]:
        return []
    pivot=sorted[0]
    before=qsort(filter(lambda x:x<=pivot,sorted[1:]))
    after =qsort(filter(lambda x:x>pivot,sorted[1:]))
    return before+[pivot]+after

sort=[random.randint(0,100) for i in range(100)]
sorted=qsort(sort)
print sorted