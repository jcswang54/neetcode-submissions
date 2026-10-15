class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                        # same first number as before: skip

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                  # skip repeated second numbers
        return result

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        i = 0

        for i in range(length):
            j = i+1
            while j > i and j <length:
                k = j+1
                while k > j and k< length:
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j],nums[k]])
                        break
                    else:
                        k +=1
                j += 1
        return result
"""
                    
