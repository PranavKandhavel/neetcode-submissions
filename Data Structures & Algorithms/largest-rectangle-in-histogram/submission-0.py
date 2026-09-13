class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        stack.append(0)
        max_area = 0
        for i in range(1,len(heights)):
            if heights[i] < heights[stack[-1]]:
                while stack and heights[stack[-1]] > heights[i] :
                    curr_height = heights[stack.pop()]
                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i
                    area = curr_height * width
                    max_area = max(area,max_area)
            stack.append(i)
        if stack:
            while stack:
                i = len(heights)
                curr_height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = curr_height * width
                max_area = max(area,max_area)
        return max_area