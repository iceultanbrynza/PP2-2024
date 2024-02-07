def unique(lists):
    dict = {}
    l1 = []
    for i in lists:
        dict[i] = 0
        l1 = list(dict.keys())
    return l1
    
l = [1, 2, 3, 3, 4, 4, 5]
print(unique(l))

#printing unique elements without set