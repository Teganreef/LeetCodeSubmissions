class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        i = 0
        occr = 0 
        for j in range(len(s)):
            if s[j] not in tracker:
                tracker[s[j]] = j
            elif s[j] in tracker:
                i = max(i, tracker[s[j]] + 1)
                tracker[s[j]] = j
            occr = max(occr,(j-i) + 1)
        return occr 