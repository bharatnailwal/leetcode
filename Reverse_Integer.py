# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(x)[::-1])
        if l[-1] == "-":
            l.pop()
            l.insert(0,"-")
        elif l[0] == "-":
            l.pop(0)
            l.insert(-1,"-")
        range1=[-2**31,2**31-1]
        s=int(''.join(l))
        if (s<range1[0] or s>range1[1]):
            return 0
        return s
