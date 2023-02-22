class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        answer = 0
        dic = defaultdict()
        for i in range(len(s)):
            if s[i] in dic:
                answer = max(answer,i-index)
                index = max(index,dic[s[i]] + 1)
                dic[s[i]] = i
            else:
                dic[s[i]] = i
        return max(answer, len(s) - index)
            