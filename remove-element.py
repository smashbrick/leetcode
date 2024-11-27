##Python

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # This will track the index for valid elements

        for i in range(len(nums)):  # Iterate over the entire list
            if nums[i] != val:  # If the current element is not equal to val
                nums[k] = nums[i]  # Move valid element to the k-th position
                k += 1  # Increment the count of valid elements

        return k  # Return the count of valid elements


## JavasScript
# /**
#  * @param {number[]} nums
#  * @param {number} val
#  * @return {number}
#  */
# var removeElement = function(nums, val) {
#     let k = 0;

#     for (let i = 0; i < nums.length; i++){
#         if (nums[i] != val){
#             nums[k] = nums[i]
#             k+=1
#         }
#     }
#     return k
# };
