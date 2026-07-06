class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                if pairs[ch] != stack[-1]:
                    return False
                
                stack.pop()
        
        return not stack