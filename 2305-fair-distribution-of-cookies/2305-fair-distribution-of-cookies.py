class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        answer = inf
        cookies.sort(reverse = True)
        def split_cookies(index,childs):
            nonlocal answer
            if answer == max(childs):
                return 
            if index == len(cookies):
                answer = min(answer,max(childs))
                return
            for i in range(k):
                childs[i] += cookies[index]
                split_cookies(index + 1,childs)
                childs[i] -= cookies[index]
            return 
        split_cookies(0,[0]*k)
        return answer
                
                