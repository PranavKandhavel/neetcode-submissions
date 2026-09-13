from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict1 = Counter(s1)
        win_size = len(s1)
        l = 0
        r = win_size
        for i in range(len(s2)):
            dict2 = Counter(s2[l:r])

            if dict1 == dict2:
                return True
            l += 1
            r+= 1
        return False
        