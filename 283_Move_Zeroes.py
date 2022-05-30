class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        dt = 0
        if len(nums) == 0 and num[0] ==0:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[dt],nums[i] = nums[i],nums[dt]
                    dt+=1
            return nums
