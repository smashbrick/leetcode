class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # This will count the number of valid elements

        for i, num in enumerate(nums):
            if num != val:
                nums[k] = num  # Move valid element to the front
                k += 1  # Increment count of valid elements
        
        print(nums[:k])  # This will show only valid elements
        return k
