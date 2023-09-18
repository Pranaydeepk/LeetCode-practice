class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count, empty = 0, 0
        while True:
            count += numBottles
            empty += numBottles
            numBottles = 0
            numBottles = empty // numExchange
            empty = empty % numExchange
            if numBottles == 0:
                break
        return count