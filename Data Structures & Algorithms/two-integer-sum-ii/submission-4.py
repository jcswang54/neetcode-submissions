class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}                                   # value -> index
        for i, value in enumerate(numbers):
            if target - value in seen:
                return [seen[target - value] + 1, i + 1]
            seen[value] = i