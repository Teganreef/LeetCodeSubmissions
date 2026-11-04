class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lst_val = prices[0]
        hst_val = 0 
        for values in prices:
            if values < lst_val:
                lst_val = values 
            if values - lst_val > hst_val :
                hst_val = values - lst_val 
        return hst_val
                
        