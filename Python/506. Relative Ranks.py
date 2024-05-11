class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = []
        for i, s in enumerate(score):
            temp.append((s, i))
            
        temp.sort(key=lambda x: x[0], reverse=True)
        
        for i in range(len(temp)):
            if i == 0:
                score[temp[i][1]] = "Gold Medal"
            elif i == 1:
                score[temp[i][1]] = "Silver Medal"
            elif i == 2:
                score[temp[i][1]] = "Bronze Medal"
            else:
                score[temp[i][1]] = str(i+1)
        return score

