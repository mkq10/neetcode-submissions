class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, j in enumerate(nums):
            d = target - j
            if d in map:
                return [map[d], i]
            map[j] = i