from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pointer1 = nums[0]
        pointer2 = nums[nums[0]]
        # position pointer2 at the point the 2 pointers meet
        while pointer2 != pointer1:
            pointer2 = nums[nums[pointer2]]
            pointer1 = nums[pointer1]

        # start pointer 1 from the beginning
        pointer1 = 0
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        return pointer1

array = [1,3,4,2,2]

solution = Solution()

print(solution.findDuplicate(array))