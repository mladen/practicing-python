class SuperList:
    def __init__(self, number):
        self.numbers = [number]

    def __len__(self):
        return 1000

    # def addNumber(self, number):
    #     self.numbers.append(number)

    def append(self, number):
        self.numbers.append(number)

    def getNumberByPosition(self, position):
        return self.numbers[position]


sl = SuperList(4)
# sl.addNumber(7)
sl.append(7)
# print(len([3, 2, 3]))
print(len(sl))
print(f"Number on 2nd position is: {sl.getNumberByPosition(1)}")
