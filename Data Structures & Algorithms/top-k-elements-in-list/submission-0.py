import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        heap = []

        for num in freq:
            heapq.heappush(heap,(freq[num],num))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        for frequency,num in heap:
            ans.append(num)

        return ans