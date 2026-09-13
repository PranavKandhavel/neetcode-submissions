from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0

        dict1 = Counter(t)
        win = Counter()

        having = 0
        need = len(dict1)

        min_lenn = float('inf')
        min_start = 0

        for r in range(len(s)):
            win[s[r]] += 1

            if s[r] in dict1 and win[s[r]] == dict1[s[r]]:
                having += 1

            while having == need:

                lenn = r - l + 1

                if lenn < min_lenn:
                    min_lenn = lenn
                    min_start = l

                if s[l] in dict1 and win[s[l]] == dict1[s[l]]:
                    having -= 1

                win[s[l]] -= 1
                l += 1

        if min_lenn == float('inf'):
            return ""

        return s[min_start:min_start + min_lenn]