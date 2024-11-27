//Javascript

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
	mySet = new Set();
	let k = 0;

	for (let i = 0; i < nums.length; i++) {
		if (!mySet.has(nums[i])) {
			mySet.add(nums[i]);
			nums[k] = nums[i];
			k += 1;
		}
	}
	return k;
};

//Python
// class Solution:
//     def removeDuplicates(self, nums: List[int]) -> int:
//         mySet = set()
//         k = 0

//         for i in range(len(nums)):
//             if nums[i] not in mySet:
//                 mySet.add(nums[i])
//                 nums[k] = nums[i]
//                 k+=1

//         return k
