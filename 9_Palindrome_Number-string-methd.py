# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
   
    x = str(x)
    aux = len(x) - 1
    exit = True
    for i in range(len(x)//2):
        if x[i] != x[aux]:   
            exit = False
        aux -= 1          
    return exit
