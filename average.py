class AverageStream:
    
    def __init__(self):
        self.numbers = []
        self.counts = 0

    def add_element(self, number):
        self.numbers.append(number)
        self.counts += 1

    def get_average(self):
        total = 0
        for num in range(0, len(self.numbers)):
            total = total + self.numbers[num]

        print(total / self.counts)

avg_inst = AverageStream()
avg_inst.add_element(5)
avg_inst.add_element(15)
avg_inst.get_average()