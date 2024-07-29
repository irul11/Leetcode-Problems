class Fenwick:

    def __init__(self,n):
        self.arr = [0]*(1+n)
        self.n = n
        self.k = 0
    
    def update(self,i,delta):
        self.k+=delta
        while i<=self.n:
            self.arr[i] += delta
            i += i & -i
    
    def query(self,i):
        ct = 0
        while i:
            ct += self.arr[i]
            i -= i & -i
        return ct

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        k = len(rating)
        nums = [None]*k
        for i,x in enumerate(sorted(range(k),key = lambda x:rating[x])):
            nums[x] = i+1

        left = Fenwick(k)
        right = Fenwick(k)

        left.update(nums[0],1)
        for i in range(1,k):
            right.update(nums[i],1)
        
        res = 0
        for i in range(1,k-1):
            right.update(nums[i],-1)

            left_less = left.query(nums[i]-1)
            right_less = right.query(nums[i]-1)
            left_greater = i-left_less
            right_greater = k-1-i-right_less
            res += left_less*right_greater + left_greater*right_less

            left.update(nums[i],1)
        return res