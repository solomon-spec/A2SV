class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(words) != len(pattern):
            return False
        hashmap = defaultdict(str)
        word = set()
        for i in range(len(pattern)):
            if words[i] not in word:
                hashmap[pattern[i]] = words[i]
                word.add(words[i])
        
        for i in range(len(pattern)):
            if hashmap[pattern[i]] != words[i]:
                return False
        print(hashmap)
        return True

