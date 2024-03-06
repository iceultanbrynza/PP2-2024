import os
path = './txtfile/'
def range_for_letters(l1, l2):
    return [chr(n) for n in range( ord(l1), ord(l2)+1)]
for i in range_for_letters('A', 'Z'):
    with open(path + f"{i}.txt", "w") as file:
        file.write('New txt created')
