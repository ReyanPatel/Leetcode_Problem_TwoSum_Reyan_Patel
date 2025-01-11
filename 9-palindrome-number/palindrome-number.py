class Solution:

    def isPalindrome(self, x:str):

        x_str=str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False