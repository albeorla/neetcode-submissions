class Solution:
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        answers = [0] * n
        stack = []

        for i in range(n):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                day = stack.pop()
                answers[day] = i - day
        
            stack.append(i)
    
        return answers