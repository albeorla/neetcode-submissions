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
                
                top = stack[-1]
                if pairs[ch] != top:
                    return False
                
                stack.pop()
        
        return not stack