class MedianFinder:
    def __init__(self):
        self.list_of_number = []
        self.return_values = []
        self.return_values.append(None)

    def addNum(self, num: int) -> None:
        self.list_of_number.append(num)
        self.return_values.append(None)

    def findMedian(self):
        self.list_of_number.sort()
        if len(self.list_of_number) == 1:
            return self.list_of_number[0]
        return self.list_of_number[int((len(self.list_of_number)-1)/2)] if len(self.list_of_number)%2 == 1 else (self.list_of_number[int(len(self.list_of_number)/2)-1] + self.list_of_number[int(len(self.list_of_number)/2)])/2

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.findMedian()
medianFinder.addNum(3) 
medianFinder.findMedian()