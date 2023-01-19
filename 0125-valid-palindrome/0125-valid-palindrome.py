class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lp= 0
        rp = len(s)-1
        letters = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9'}
        while lp <= rp:
            if upper(s[lp]) not in letters and upper(s[rp]) not in letters:
                lp += 1
                rp -=1
            elif upper(s[lp]) not in letters:
                lp += 1
            elif upper(s[rp]) not in letters:
                rp -= 1
            else:
                if upper(s[lp]) == upper(s[rp]):
                    lp += 1
                    rp -= 1
                else:
                    return False
        return True
