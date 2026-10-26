class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total_nums = len(nums)
        res = []
        for i in range(total_nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, total_nums - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res