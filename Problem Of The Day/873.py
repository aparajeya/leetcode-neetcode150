class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Create a set of all the elements in the array for O(1) look-up
        possible_sum_set = set(arr)
        
        # Initialize the variables to keep track of the longest Fibonacci subsequence
        max_len = 0   # This will store the maximum length of the Fibonacci subsequence
        curr_len = 0  # This will store the current length of the Fibonacci subsequence
        
        # Iterate over all pairs (i, j) in the array, where i < j
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):  # Start from j = i + 1 to avoid duplicates
                num1 = arr[i]  # The first number in the Fibonacci sequence
                num2 = arr[j]  # The second number in the Fibonacci sequence
                num_sum = num1 + num2  # The sum of num1 and num2 (the next number in the sequence)
                
                # Check if the sum exists in the set (i.e., it's a valid next number in the sequence)
                while num_sum in possible_sum_set:
                    # If the sum is found in the set, we have a valid Fibonacci subsequence
                    curr_len += 1  # Increase the length of the current subsequence
                    # Update num1 and num2 to move forward in the sequence
                    num1 = num2
                    num2 = num_sum
                    num_sum = num1 + num2  # The new sum becomes the next number in the sequence
                    
                    # Update max_len if the current subsequence is the longest found so far
                    if curr_len >= max_len:
                        max_len = curr_len
                
                # Reset the current length after finishing the while loop for the pair (i, j)
                curr_len = 0
        
        # If no Fibonacci subsequence was found, return 0
        if max_len == 0:
            return 0
        else:
            # Return the length of the longest Fibonacci subsequence found, which is max_len + 2
            # because the loop counts the first two elements (arr[i] and arr[j]) as part of the subsequence
            return max_len + 2
