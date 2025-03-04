class Solution:
    def checkValidCombinations(
        self, valid_coin_combination, running_sum, coins_values, index
    ):
        """
        Recursively generates all possible sums using the given coin values.
        
        Args:
        valid_coin_combination (list): Stores all possible sums that can be formed.
        running_sum (int): Current sum being calculated.
        coins_values (list): List of available coin values (powers of 3 in this case).
        index (int): Current index in coins_values list.
        """
        if index == len(coins_values):  # Base case: If index reaches the end, store the sum
            valid_coin_combination.append(running_sum)
            return
        
        # Include the current coin in the sum
        running_sum += coins_values[index]
        self.checkValidCombinations(
            valid_coin_combination, running_sum, coins_values, index + 1
        )
        
        # Backtrack: Remove the current coin from the sum
        running_sum -= coins_values[index]
        
        # Exclude the current coin and move to the next
        self.checkValidCombinations(
            valid_coin_combination, running_sum, coins_values, index + 1
        )
        
        return

    def checkPowersOfThree(self, n: int) -> bool:
        """
        Checks if the given number n can be represented as a sum of distinct powers of 3.
        
        Args:
        n (int): The number to check.
        
        Returns:
        bool: True if n can be represented as a sum of distinct powers of 3, otherwise False.
        """
        coins_values = []  # List to store powers of 3
        valid_coin_combination = []  # List to store all possible sums
        
        # Generate all powers of 3 up to a reasonable limit (10^7 here)
        coins_value = 1  # First power of 3
        while coins_value < 10000000:
            coins_values.append(coins_value)
            coins_value *= 3  # Move to the next power of 3
        
        running_sum = 0  # Initialize sum as 0
        index = 0  # Start recursion from index 0
        
        # Generate all valid sums using the recursive function
        self.checkValidCombinations(
            valid_coin_combination, running_sum, coins_values, index
        )
        
        # Check if n is present in the generated valid sums
        return n in valid_coin_combination
