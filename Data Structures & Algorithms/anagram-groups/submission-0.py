class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in range(len(strs)):
            sortt = ''.join(sorted(strs[i]))

            if sortt in dict1:
                dict1[sortt].append(strs[i])
            else:
                dict1[sortt] = [strs[i]]

        return list(dict1.values())