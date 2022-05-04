#Example 1:
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
        return count
