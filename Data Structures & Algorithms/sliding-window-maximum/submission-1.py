import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        max_heap = []
        output = []
        for r in range(len(nums)):
            heapq.heappush(max_heap,(-nums[r],r))
            if r - l + 1 == k:
                output.append(-max_heap[0][0])
                l += 1
                while max_heap and max_heap[0][1] < l:
                    heapq.heappop(max_heap)

        return output
