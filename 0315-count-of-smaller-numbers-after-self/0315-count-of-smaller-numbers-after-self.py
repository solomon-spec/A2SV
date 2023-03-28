class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        new_arr = [(i,j) for i,j in enumerate(nums)]
        dic = defaultdict(int)
        
        def merge(arr):
            nonlocal dic
            if len(arr) == 1:
                return arr
            
            right = merge(arr[len(arr)//2:])
            left = merge(arr[:len(arr)//2])
            
            
            ans = []
            l = r = 0
            
            while l < len(left) or r < len(right):
                if l >= len(left) or (r < len(right) and left[l][1] > right[r][1]):
                    ans.append(right[r])
                    r += 1
                else:
                    ans.append(left[l])
                    dic[left[l][0]] += (len(ans) - l - 1)
                    l += 1
            return ans
        merge(new_arr)
        answer = []
        for i , j in sorted(dic.items()):
            answer.append(j)
        return answer + [0]
        
                