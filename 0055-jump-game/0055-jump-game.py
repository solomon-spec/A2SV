class Solution:
    def canJump(self, nums: List[int]) -> bool:
        queue = deque([0])
        cur_pos = 0
        target = len(nums)-1
        while queue:
            if cur_pos == target: return True
            x = queue.popleft()
            steps = x + nums[x] - cur_pos
            while steps > 0:
                cur_pos+= 1
                if cur_pos < len(nums):queue.append(cur_pos)
                if cur_pos == target: return True
                steps -= 1
        return False
                