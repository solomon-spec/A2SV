class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = defaultdict(int)
        answer = []
        
        for number in nums1:
            hashmap[number] += 1
        
        for number in nums2:
            if hashmap[number] > 0:
                answer.append(number)
                hashmap[number] -= 1
        return answer