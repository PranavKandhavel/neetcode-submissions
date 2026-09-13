class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        stack.append(0)
        for i in range(1,len(temperatures)):
            if stack and temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    a = stack.pop()
                    output[a] = i - a
                stack.append(i)

        return output