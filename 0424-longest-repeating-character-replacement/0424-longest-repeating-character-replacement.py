class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = defaultdict(int)
        maxlength = 0
        if len(set(s)) == 1:
            return len(s)

        for r in range(len(s)):
            hashmap[s[r]]+=1
            print(hashmap)

            while max(hashmap.values()) + k < (r - l + 1) :
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
            maxlength=max(maxlength,r-l+1)
        return maxlength