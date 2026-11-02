class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_list = str(x) # first part trunign it into a new list 
        l = 0
        r = (len(new_list) - 1)
        while l < r:
            if new_list[l] != new_list[r]:
                return False 
            l += 1
            r += -1
        return True 
        