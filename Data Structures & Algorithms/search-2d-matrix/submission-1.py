class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums):
            l = 0
            r = len(nums) - 1
            mid = len(nums) // 2

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
            
        for i in range(len(matrix)):
            ans = binary_search(matrix[i])
            if ans != -1:
                return True
        return False