class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        c_dict = {}
        for num in nums:
            if num not in c_dict:
                c_dict[num] = 1 
            else: return True
        return False

        