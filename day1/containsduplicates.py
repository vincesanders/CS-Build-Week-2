class Solution:
    def containsDuplicate(self, nums):
        # Create a set to keep track of nums already encountered in the array
        visited = set()
        
        # Iterate through the list
        for num in nums:
            
            # if the number is already in the set, 
            # that means we have a duplicate and can return True.
            if num in visited:
                return True
            # If the number isn't in the set, add it
            else:
                visited.add(num)
                
        # If we get to this point, we haven't found any duplicates.
        return False