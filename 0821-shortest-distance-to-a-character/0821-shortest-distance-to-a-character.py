class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        arr  = []
        for i in range(len(s)):
            if s[i] == c:
                arr.append(i)
        prev = None
        cur = 0
        answer = []
        for i in range(len(s)):
            if prev == None or abs(i - arr[prev]) > abs(i - arr[cur]):
                answer.append(abs(i - arr[cur]))
            else:
                answer.append(abs(i - arr[prev]))
            if s[i] == c:
                cur = cur + 1 if cur + 1 < len(arr) else cur
                prev = 0 if prev == None else prev + 1 if prev + 1 < len(arr) else prev
        return answer