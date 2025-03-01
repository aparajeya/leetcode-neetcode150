class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nums_non_zero = []  # List to store non-zero elements after processing
        nums_zero = []  # List to store zero elements separately

        # Iterate through the array except for the last element
        for i in range(len(nums) - 1):
            # If two consecutive elements are equal, merge them
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]  # Double the value of the first element
                nums[i + 1] = 0  # Set the second element to zero
            
            # Store non-zero and zero elements separately
            if nums[i] != 0:
                nums_non_zero.append(nums[i])  # Add non-zero element to nums_non_zero
            else:
                nums_zero.append(0)  # Add zero element to nums_zero

        # Handle the last element separately
        if nums[i + 1] != 0:
            nums_non_zero.append(nums[i + 1])
        else:
            nums_zero.append(0)

        # Concatenate non-zero elements followed by zero elements
        return nums_non_zero + nums_zero
