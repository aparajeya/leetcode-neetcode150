class Solution:
    # Helper function to find the largest sum of a contiguous subarray (Kadane's Algorithm)
    def findLargestSum(self, nums: List[int]) -> int:
        running_sum = 0  # Variable to store the sum of the current subarray
        largest_sum = 0  # Variable to store the largest sum found so far
        
        # Iterate through the array
        for i in range(len(nums)):
            running_sum += nums[i]  # Add the current element to the running sum
            
            # If running_sum becomes negative, reset it to 0 (start a new subarray)
            if running_sum < 0:
                running_sum = 0
            
            # Update the largest_sum if the running_sum is greater than the current largest_sum
            if running_sum > largest_sum:
                largest_sum = running_sum
        
        # Return the largest sum found
        return largest_sum
    
    # Function to find the maximum absolute sum of any subarray
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Find the largest sum of a contiguous subarray (positive sum)
        value1 = self.findLargestSum(nums)
        
        # Negate all elements of the array to handle absolute value of subarray sum
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]  # Flip the sign of each element
        
        # Find the largest sum of a contiguous subarray in the negated array
        value2 = self.findLargestSum(nums)
        
        # Return the maximum of the two sums (one for positive subarrays and one for negative subarrays)
        return max(value1, value2)
