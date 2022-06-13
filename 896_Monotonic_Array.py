# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:     
        val1 = True
        val2 = True
        for i in range(len(nums)-1):
            if (nums[i+1] > nums[i]):
                val1 = False
        for i in range(len(nums)-1):
            if (nums[i] > nums[i+1]):               
                val2 = False            
        if val1 or val2:
            return True
        else:
            return False
