#Example 1:
#Input: nums = [1,1,2]
#Output: 2, nums = [1,2,_]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count+=1
        return count
