# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:          
# METHOD 1
#         nums = sorted(nums)
#         for i in range (1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True           
#         return False    
# METHOD 2
        s = set(nums)
        if len(s)==len(nums):
            answer = False
        else:
            answer = True
        return answer
