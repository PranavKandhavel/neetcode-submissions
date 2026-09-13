class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        ans_l = 1
        for i in range(len(nums)):
            left.append(ans_l)
            ans_l = ans_l * nums[i]
        ans_r = 1
        right = [0] * len(nums)
        for i in range(len(nums) - 1,-1,-1):
            right[i] = ans_r * left[i]
            ans_r = ans_r * nums[i]
        return right