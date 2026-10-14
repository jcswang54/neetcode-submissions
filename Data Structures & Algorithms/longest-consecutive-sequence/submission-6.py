class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) ==1:
                return 1
        if len(nums_set) ==0:
                return 0
        result = 1
        for x in nums_set:
            if x-1 not in nums_set:
                j = 1 
                while x+j in nums_set:
                    j+= 1
                    result = max(j, result)
        return result
