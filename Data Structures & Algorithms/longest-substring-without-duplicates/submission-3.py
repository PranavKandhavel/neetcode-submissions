class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        lenn = 0

        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l += 1

            sett.add(s[i])
            lenn = max(lenn, i - l + 1)

        return lenn