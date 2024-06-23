class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        deq = deque(sorted(nums))
        ans = float(inf)
        
        for i in range(len(nums) // 2):
            ans = min((deq[0] + deq[-1])/2, ans)
            deq.pop()
            deq.popleft()
            
        return ans
    