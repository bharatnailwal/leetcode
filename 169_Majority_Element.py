# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:           
        nums = sorted(nums)
        dt = {}
        ln = len(nums)/2
        for i in nums:
            if i in dt:
                dt[i] +=1
            else:
                dt[i] = 1
        for j,k in dt.items():
            if k >=ln:
                return j
