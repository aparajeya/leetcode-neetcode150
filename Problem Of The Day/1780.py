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
    
# Below is the efficient solution
'''
The question is essentially asking us to to figure out whether a number
can be represented by a base 3 ternary system where none of the powers 
of 3 are duplicated, i.e. the powers of 3 must be distinct.

Note that for example 3, n = 21 can be represented as 
2 * (3 ^ 2) + 1 * (3 ^ 1) + 0 * (3 ^ 0), or (210)_3 in base 3. 
The 2 coefficient here is the problem because that means we 
don't have distinct powers of 3. Try doing the same thing you
would when converting a number to binary, except, instead of using 2, 
we are using 3 as the base here.

Below is the solution for reference
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n!=0):
            if(n%3>1):
                return False
            n=n//3
        return True
