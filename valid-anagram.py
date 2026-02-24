class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freqs = {}
        freqt = {}
        for char in s:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
        for char in t:
            if char in freqt:
                freqt[char] += 1
            else:
                freqt[char] = 1
        return freqs == freqt

#Different solution
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)