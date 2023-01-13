class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxx = 0
        for lists in accounts:
            total = sum(lists)
            if total > maxx:
                maxx = total
        return maxx