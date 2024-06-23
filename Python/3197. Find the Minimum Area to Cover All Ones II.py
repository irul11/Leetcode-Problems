class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        gs = [[0] * (n + 1)]
        for r in grid:
            gs.append([i + j for i, j in zip(gs[-1], accumulate(r, initial=0))])

        def cnt(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return 0
            return gs[i2 + 1][j2 + 1] - gs[i2 + 1][j1] - gs[i1][j2 + 1] + gs[i1][j1]
        
        def shrink(i1, i2, j1, j2):
            org = cnt(i1, i2, j1, j2)
            if org == 0:
                return  # None if empty (invalid)
            while cnt(i1 + 1, i2, j1, j2) == org:
                i1 += 1
            while cnt(i1, i2 - 1, j1, j2) == org:
                i2 -= 1
            while cnt(i1, i2, j1 + 1, j2) == org:
                j1 += 1
            while cnt(i1, i2, j1, j2 - 1) == org:
                j2 -= 1
            return i1, i2, j1, j2
        
        def vsplit(i1, i2, j1, j2):
            for x in range(j1, j2):
                p1 = shrink(i1, i2, j1, x)
                p2 = shrink(i1, i2, x + 1, j2)
                if p1 is None or p2 is None:
                    continue
                yield p1, p2
        
        def hsplit(i1, i2, j1, j2):
            for x in range(i1, i2):
                p1 = shrink(i1, x, j1, j2)
                p2 = shrink(x + 1, i2, j1, j2)
                if p1 is None or p2 is None:
                    continue
                yield p1, p2
        
        def area(i1, i2, j1, j2):
            return (i2 - i1 + 1) * (j2 - j1 + 1)
        
        ans = inf        
        p = shrink(0, m-1, 0, n-1)
        for sp1, sp2 in product((vsplit, hsplit), repeat=2):
            for p1, p2 in sp1(*p):
                ans = min(ans, area(*p1) + min((area(*pa) + area(*pb) for pa, pb in sp2(*p2)), default=inf))
                if sp1 is not sp2:  # if different, we should try to split both subpart
                    ans = min(ans, area(*p2) + min((area(*pa) + area(*pb) for pa, pb in sp2(*p1)), default=inf))
        return ans
    