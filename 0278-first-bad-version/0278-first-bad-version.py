# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l<r:
            if isBadVersion((l+r)//2):
                r = (l+r)//2 - 1
            else:
                l = (l+r)//2 + 1
        if isBadVersion(l):
            return l
        else:
            return l + 1
        