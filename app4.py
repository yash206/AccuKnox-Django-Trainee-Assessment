class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.cur_iter = 0

    def __iter__(self):
        self.cur_iter = 0
        return self

    def __next__(self):
        if self.cur_iter == 0:
            self.cur_iter += 1
            return {'length': self.length}
        elif self.cur_iter == 1:
            self.cur_iter += 1
            return {'width': self.width}
        else:
            raise StopIteration

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rect = Rectangle(length, width)
print("Dimensions of the rectangle: ")
for dim in rect:
    print(dim)