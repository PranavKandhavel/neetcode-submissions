class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max_len = 0

        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
        
        for numb in seen:
            curr = numb
            if numb - 1 not in seen:
                lenn = 0
                curr += 1
                while curr in seen:
                    lenn += 1
                    curr += 1

                max_len = lenn if lenn > max_len else max_len

        return max_len + 1