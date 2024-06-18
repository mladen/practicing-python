class SuperList(list):
    # NOTE: We don't need this now that we're inheriting from the "list" (the "list" is the superclass now)
    # def __init__(self, number):
    #     self.numbers = [number]

    def __len__(self):
        return 1000

    # NOTE: We don't need this now that we're inheriting from the "list" (the "list" is the superclass now)
    # def append(self, number):
    #     self.numbers.append(number)

    # NOTE: We don't need this now that we're inheriting from the "list" (the "list" is the superclass now)
    # def getNumberByPosition(self, position):
    #     return self.numbers[position]


sl = SuperList()
print(len(sl))

# sl.addNumber(7)
sl.append(7)
sl.append(4)
# print(len([3, 2, 3]))
# print(f"Number on 2nd position is: {sl.getNumberByPosition(1)}")
print(f"Number on 2nd position is: {sl[1]}")
