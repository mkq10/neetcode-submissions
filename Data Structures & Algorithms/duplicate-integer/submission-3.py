class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        return True if len(nums) != len(map) else False

        # Solution 1
        ''' nums.sort()
        for i in range(len(nums)):
            if i+1 == len(nums):
                break;

            curr = nums[i]
            next = nums[i+1]
            if curr == next:
                return True 

        return False '''