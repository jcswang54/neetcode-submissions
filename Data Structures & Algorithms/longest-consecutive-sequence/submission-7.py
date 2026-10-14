class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                j = 1
                while x + j in nums_set:
                    j += 1
                result = max(result, j)
        return result