class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(int)
        ans, maxx = "", 0

        for i in range(len(messages)):
            counter[senders[i]] += len(messages[i].split())
            if maxx < counter[senders[i]]:
                ans = senders[i]
                maxx = counter[senders[i]]
            elif maxx == counter[senders[i]] and ans < senders[i]:
                ans = senders[i]
        
        
        return ans
        