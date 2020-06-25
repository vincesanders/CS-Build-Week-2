from typing import List

class Solution:
    def binary_recursive_search(self, nums: List[int], target: int, low=0) -> int:
        if len(nums) < 1:
            return None
        elif len(nums) is 1 and nums[0] != target:
            return None
        else:
            middle = (len(nums) - 1) // 2
            if target == nums[middle]:
                return low + middle
            else:
                index = self.binary_recursive_search(nums[:middle], target, low)
                if index is None:
                    index = self.binary_recursive_search(nums[middle + 1:], target, low + middle + 1)
                else:
                    return index
                if index is not None:
                    return index

    def search(self, nums: List[int], target: int) -> int:
        found_at_index = self.binary_recursive_search(nums, target)
        if found_at_index is None:
            return -1
        else:
            return found_at_index

array = [4,5,6,7,0,1,2]
solution = Solution()

print(solution.search(array, 2))