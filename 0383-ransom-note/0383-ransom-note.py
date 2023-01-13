class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = defaultdict(int)
        
        for letter in magazine:
            hashmap[letter] += 1
        
        for letter in ransomNote:
            hashmap[letter] -= 1
            if hashmap[letter] < 0:
                return False
        return True