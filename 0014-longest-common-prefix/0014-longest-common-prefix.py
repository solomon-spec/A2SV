class Solution(object):
    def longestCommonPrefix(self, strs):
        strr = sorted(strs)
        minn = min(len(ele) for ele in strr)
        common = ""
        for i in range(minn):
            if strr[0][i]==strr[len(strr)-1][i]:
                common+=strr[0][i]
            else:
                break
        return common
      
        