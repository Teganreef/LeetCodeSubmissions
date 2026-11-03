class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char not in hash_map:
                stack.append(char)
            else:
                if not stack:
                        return False 
                else:
                    popped = stack.pop()
                    if popped != hash_map[char]:
                        return False
        return not stack

                





        