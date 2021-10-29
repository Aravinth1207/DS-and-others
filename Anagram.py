from collections import Counter
def anagram(x,y):
    return len(x)+len(y)-sum((Counter(x)&Counter(y)).values())*2
print(anagram('abcd','cdef'))
