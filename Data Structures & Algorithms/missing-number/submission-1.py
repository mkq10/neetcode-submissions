class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = 0
        nums.sort()
        for i, v in enumerate(nums):
            if miss == v:
                miss += 1
            else:
                return miss

        return miss