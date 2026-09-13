from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = Counter()
        l = 0
        lenn = 0
        max_freq = 0

        for r in range(len(s)):
            char_freq[s[r]] += 1
            max_freq = max(max_freq, char_freq[s[r]])

            while (r - l + 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1

            lenn = max(lenn, r - l + 1)

        return lenn