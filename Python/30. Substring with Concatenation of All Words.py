from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        counter_words = Counter(words)
        length_words = len(words)
        length_element = len(words[0])
        length_s = len(s)
        result = []

        for i in range(length_element):
            counter_temp = Counter()
            left = right = i
            t = 0
            while right + length_element <= length_s:
                word = s[right : right + length_element]
                right += length_element
                
                if word not in counter_words:
                    left = right
                    counter_temp.clear()
                    t = 0
                    continue

                counter_temp[word] += 1                    
                t += 1

                while counter_temp[word] > counter_words[word]:
                    remove_word = s[left : left + length_element]
                    print(remove_word)
                    left += length_element                 
                    counter_temp[remove_word] -= 1 
                    t -= 1
                if t == length_words:
                    result.append(left)
        
        return result
    

if __name__ == "__main__":
    solution = Solution()
    # For testing
    # print(solution.findSubstring(
    #     s = "wordgoodgoodgoodbestword", 
    #     words = ["word","good","best","word"]
    # ))