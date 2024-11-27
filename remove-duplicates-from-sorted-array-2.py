#Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myDict = {}
        k = 0

        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = 1
                nums[k] = nums[i]
                k+=1
            elif nums[i] in myDict and myDict[nums[i]]  == 1:
                myDict[nums[i]] = 2
                nums[k] = nums[i]
                k+=1
            elif nums[i] in myDict and myDict[nums[i]] > 2:
                continue
        return k           


        