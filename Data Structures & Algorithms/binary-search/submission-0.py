class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dic = {value:index for index, value  in enumerate(nums)}
        if target in dic:
            return dic[target]
        else:
            return -1
