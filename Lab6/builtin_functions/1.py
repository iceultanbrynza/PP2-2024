result = 1
def ListMulti(x):
    global result
    result = result * x
    return result
l = [1,2,3,4,5]
Elmnts_Multi = list(map(ListMulti, l))
print(Elmnts_Multi[-1])
