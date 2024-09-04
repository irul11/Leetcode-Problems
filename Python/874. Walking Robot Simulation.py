class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = defaultdict(list), defaultdict(list)
        for o in obstacles:
            x[o[0]].append(o[1])
            y[o[1]].append(o[0])
            
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0
        coor = [0, 0]
        ans = 0

        for c in commands:
            if c == -1:
                idx = (idx + 1) % 4
                
            elif c == -2:
                idx = (idx - 1) if idx - 1 >= 0 else 3
                
            else:
                if coor[0] == 0 and coor[1] == 0 and 0 in x and 0 in x[0]:
                    coor[0] += dir[idx][0] * c
                    coor[1] += dir[idx][1] * c
                elif coor[0] in x and idx % 2 == 0:
                    miny = min(coor[1], coor[1] + dir[idx][1] * c)
                    maxy = max(coor[1], coor[1] + dir[idx][1] * c)
                    temp = [inf, -inf]
                    for yy in x[coor[0]]:
                        if miny <= yy <= maxy:
                            temp[0] = min(temp[0], yy)
                            temp[1] = max(temp[1], yy)
                            
                    if temp[0] != inf and temp[1] != -inf:
                        if idx == 0:
                            coor[1] = temp[0] - 1
                        elif idx == 2:
                            coor[1] = temp[1] + 1
                    else:
                        coor[1] += dir[idx][1] * c

                elif coor[1] in y and idx % 2 != 0:
                    minx = min(coor[0], coor[0] + dir[idx][0] * c)
                    maxx = max(coor[0], coor[0] + dir[idx][0] * c)
                    temp = [inf, -inf]
                    for xx in y[coor[1]]:
                        if minx <= xx <= maxx:
                            temp[0] = min(temp[0], xx)
                            temp[1] = max(temp[1], xx)
                            
                    if temp[0] != inf and temp[1] != -inf:
                        if idx == 1:
                            coor[0] = temp[0] - 1
                        elif idx == 3:
                            coor[0] = temp[1] + 1
                    else:
                        coor[0] += dir[idx][0] * c

                else:
                    coor[0] += dir[idx][0] * c
                    coor[1] += dir[idx][1] * c

                ans = max(ans, coor[0]**2 + coor[1]**2)

        return ans