class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums):
                if (i != j and nums[i]+nums[j] == target):
                    array.append(i)
                    array.append(j)
                    return array
        
        return array