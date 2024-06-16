class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (2 * len(arr))
        self.arr = arr
        self.length = len(arr)
    
    def build(self):
        for i in range(1, self.length - 1):
            if self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                self.tree[self.length + i] = 1

        for i in range(self.length-1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
    
    def updateTree(self, index, value):
        self.arr[index] = value
        for i in range(index-1, index + 2):
            if i - 1 >= 0 and i + 1 < self.length:
                if self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                    self.tree[self.length + i] = 1
                else:
                    self.tree[self.length + i] = 0

                j = i + self.length
                while j > 1 : 
                    self.tree[j >> 1] = self.tree[j] + self.tree[j ^ 1];  
                    j >>= 1
                
    
    def query(self, l, r):
        res = 0;  
      
        # loop to find the sum in the range  
        l += self.length + 1; 
        r += self.length; 
        
        while l < r :
            if (l & 1) : 
                res += self.tree[l];  
                l += 1
        
            if (r & 1) : 
                r -= 1; 
                res += self.tree[r];  
                
            l >>= 1; 
            r >>= 1
        
        return res; 

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        stree = SegmentTree(nums)
        stree.build()
        
        for q in queries:
            if q[0] == 2:
                stree.updateTree(q[1],q[2])
                continue
            ans.append(stree.query(q[1], q[2]))
        
        return ans
