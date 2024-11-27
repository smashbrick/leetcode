## My Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    

        if len(nums1) != m:
            del nums1[m: ]
            print(nums1)

        nums1.extend(nums2)
        nums1.sort()

        print(nums1)


