class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        dp = []
        for i in range(101):
            dp.append(Node(i))
        
        sets = set()
        def set_val(node):
            current_value = node.val
            for i in range(len(node.neighbors)):
                neighbor_value = node.neighbors[i].val

                if (current_value, neighbor_value) in sets:
                    continue
                sets.add((current_value, neighbor_value))
                sets.add((neighbor_value, current_value))
                
                # append neigborhood on both node (current and neighbor)
                dp[current_value].neighbors.append(dp[neighbor_value])
                dp[neighbor_value].neighbors.append(dp[current_value])
                set_val(node.neighbors[i])
                
        set_val(node)
        return dp[1]


