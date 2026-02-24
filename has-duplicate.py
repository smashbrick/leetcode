class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        return False
        
#Alternate solution 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        singles = set(nums)
        return len(nums) != len(singles)