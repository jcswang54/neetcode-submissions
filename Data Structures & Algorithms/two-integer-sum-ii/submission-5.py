class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}                                   # value -> index
        for i, value in enumerate(numbers):
            if target - value in seen:
                return [seen[target - value] + 1, i + 1]
            seen[value] = i

            """
                    seen = {}
        for ind, value in enumerate(numbers):
            seen[value] = ind
        for value in seen:
            if target - value in seen and seen[value]!= seen[target-value]:
                return [seen[value]+1, seen[target-value]+1]
            """

            """
            class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1          # sum too big: use a smaller right value
            elif s < target:
                l += 1          # sum too small: use a bigger left value
            else:
                return [l + 1, r + 1]"""