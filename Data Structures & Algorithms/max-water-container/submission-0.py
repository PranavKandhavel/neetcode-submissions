class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_height = 0
        height = 0

        while i < j:
            height = (min(heights[i],heights[j])) * (j - i)

            max_height = height if height > max_height else max_height

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_height