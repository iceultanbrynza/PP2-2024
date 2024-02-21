class MyNums:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        x = pow(self.start, 2)
        self.start+=1
        return x 

spisok = MyNums(1, 5)

for square in spisok:
    print(square)