class Solution(object):
    def twoSum(self, nums, target):
        val_dict = {} # empty dict
        for pos, val in enumerate(nums): 
            finder = target - val 
            if finder in val_dict:
                return [val_dict[finder], pos]
            val_dict[val] = pos



