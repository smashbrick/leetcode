class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] +=1

            tupleIt = tuple(count)
            if tupleIt in groups:
                groups[tupleIt].append(s)
            else:
                groups[tupleIt] = [s]
        return list(groups.values())