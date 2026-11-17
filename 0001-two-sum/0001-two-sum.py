class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for pos, value in enumerate(nums):
            finder = target - value
            if finder in seen:
                return [seen[finder], pos]
            seen[value] = pos
            





