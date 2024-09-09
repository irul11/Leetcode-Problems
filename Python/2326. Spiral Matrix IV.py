# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dirx = [0, 1, 0, -1]
        diry = [1, 0, -1, 0]
        idx = 0
        ans = [[0] * n for _ in range(m)]
        x = [0, m - 1]
        y = [0, n - 1]
        i, j = 0, 0 

        while x[0] <= x[1] and y[0] <= y[1]:
            if head:
                ans[i][j] = head.val
                head = head.next
            else:
                ans[i][j] = -1
            
            i += dirx[idx]
            j += diry[idx]

            if j > y[1]:
                x[0] += 1
                j -= 1
                i += 1
                idx = (idx + 1) % 4
            elif j < y[0]:
                x[1] -= 1
                j += 1
                i -= 1
                idx = (idx + 1) % 4
            elif i > x[1]:
                y[1] -= 1
                i -= 1
                j -= 1
                idx = (idx + 1) % 4
            elif i < x[0]:
                y[0] += 1
                i += 1
                j += 1
                idx = (idx + 1) % 4

        return ans
                