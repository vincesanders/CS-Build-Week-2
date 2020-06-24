class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to track numbers that are in the list and their in index
        values = {}
        
        # move through the array
        for i, num in enumerate(nums):
            
            # Calculate the number needed for the current number to match the target
            needed_num = target - num
            
            # search dict for needed value
            if needed_num in values:
                
                # if found, return it's index, and the current index
                return [values[needed_num], i]
            
            # Add item to dict with index
            values[num] = i