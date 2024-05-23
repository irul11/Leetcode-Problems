class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        maps = defaultdict(list[int])

        for num in nums:
            maps[num%k].append(num)
        
        result = 1

        for mod, val in maps.items():
            val.sort()
            maps2 = defaultdict(int)

            for v in val:
                maps2[v] += 1
            
            prev_element = -inf
            prev_not_taken = 1
            prev_taken = now_not_taken = now_taken = 0

            for el, freq in maps2.items():
                poss_subsets = (1 << freq) - 1

                if prev_element + k == el:
                    now_not_taken = prev_not_taken + prev_taken
                    now_taken = prev_not_taken * poss_subsets
                else:
                    now_not_taken = prev_not_taken + prev_taken
                    now_taken = (prev_not_taken + prev_taken) * poss_subsets

                prev_not_taken = now_not_taken
                prev_taken = now_taken
                prev_element = el
            
            result *= (now_not_taken + now_taken)
        
        return result - 1
        