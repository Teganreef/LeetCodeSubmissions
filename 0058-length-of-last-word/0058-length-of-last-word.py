class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        correct_value = 0 
        new_list = s.split()
        correct_value = len(new_list[-1])
        return correct_value

        
        