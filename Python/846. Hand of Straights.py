class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        counter = Counter(hand)
        list_set = list(set(hand))
        list_set.sort()

        for i in range(len(list_set)):
            if counter[list_set[i]] <= 0:
                continue        
            if counter[list_set[i]] > 0 and i >= len(list_set) - groupSize + 1:
                return False

            prev = list_set[i]
            amount_of_prev = counter[prev] 
            counter[list_set[i]] -= amount_of_prev

            for j in range(i+1, i + groupSize):
                curr = list_set[j]
                
                if curr - prev != 1 or counter[curr] < amount_of_prev:
                    return False
                
                counter[curr] -= amount_of_prev
                prev = curr
            
        return True
        