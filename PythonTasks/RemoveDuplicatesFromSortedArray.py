from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return nums[:j]

nums = [1, 2, 2, 3, 3, 3, 4, 5]
sol = Solution()
result = sol.removeDuplicates(nums)
print(len(result))  # Output: 5
print(result)  # Output: [1, 2, 3, 4, 5]
