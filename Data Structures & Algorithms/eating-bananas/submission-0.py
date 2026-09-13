class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find(k):
            ans = 0
            for i in range(len(piles)):
                ans += math.ceil(piles[i] / k)
            return ans

        max_hours = max(piles)
        min_hours = 1
        min_ans = sum(piles)
        while min_hours <= max_hours:
            mid = min_hours + (max_hours - min_hours) // 2
            ans = find(mid)

            if ans > h:
                min_hours = mid + 1
            else:
                max_hours = mid -1
        return min_hours
