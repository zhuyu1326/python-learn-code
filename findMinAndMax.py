#-*- coding:utf-8 -*-
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    if len(L) == 1:
        return (L[0], L[0])
    if len(L) >=2:
        max = L[0]
        min = L[0]
        for i in L:
            if i >= max:
                max = i
            if i <= min:
                min = i
    return max, min


L = [1, 2, 3, 4, 5 ,6 , 7, 7, 666]
print(findMinAndMax(L))