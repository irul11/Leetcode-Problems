class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        countWait = 0
        currTime = 0

        for customer in customers:
            if customer[0] > currTime:
                currTime = customer[0]
            currTime += customer[1]
            countWait += currTime - customer[0]
            # print(currTime - customer[0])
        
        return countWait / len(customers)
