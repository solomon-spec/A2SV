class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for i in range(len(arr2)):
            dic[arr2[i]]=i
        def compair(num1,num2):
            if num1 not in dic and num2 not in dic:
                if num1 < num2:
                    return -1
                else:
                    return 1
            elif num1 not in dic:
                return 1
            elif num2 not in dic:
                return -1

            elif dic[num1] < dic[num2]:
                return -1
            else:
                return 1
        arr1.sort(key = cmp_to_key(compair))
        
        return arr1
            
