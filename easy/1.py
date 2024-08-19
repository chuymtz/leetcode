"""
given an array of ints return indeces of 
the two numbers such that they add up to a speific target



"""

target = 4

arr = [2, 1, 5, 3]


hash = {k:i for i, k in enumerate(arr)}

def foo(arr, target):
    for i, a in enumerate(arr):
        b = target - a
        if (b in hash.keys()) and hash[b]>i:
            j = hash[b]
            return i, j


foo(arr, target)


prevMap = {}
for i, n in enumerate(arr):
    diff  = target - n
    if diff in prevMap:
        return prevMap[diff], prevMap[i]
    else:
        prevMap[n] = i


