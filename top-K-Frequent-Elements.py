class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for number in nums:
            if number in seen:
                seen[number] += 1
            else:
                seen[number] = 1
        kValue = sorted(seen, key=seen.get, reverse=True)[:k]
        return kValue

        