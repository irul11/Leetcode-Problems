class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        total_array = (1 + k) * k // 2
        
        if total_array > n:
            return result

        def add_sum(i, temp):
            if len(temp) == k and sum(temp) == n:
                result.append(temp)
                return
            if sum(temp) > n or i > 9 or len(temp) > k:
                return

            for j in range(i+1, 10):
                add_sum(j, temp + [j])

        add_sum(0, [])
        # print(result)
        return result

        