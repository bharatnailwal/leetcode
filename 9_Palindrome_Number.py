#Example 2:
#Input: x = -121

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if x >= 0 and y == y[::-1]:
            return True
        else:
            return False
