# O(n) solution inefficient but gets the job done for 10^6 input limit
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small_list = []  # Stores elements smaller than pivot
        large_list = []  # Stores elements greater than pivot
        count_pivot = 0  # Counter for occurrences of pivot in nums
        
        # Iterate through the list and classify elements
        for i in range(len(nums)):
            if nums[i] < pivot:
                small_list.append(nums[i])  # Add smaller elements to small_list
            elif nums[i] > pivot:
                large_list.append(nums[i])  # Add larger elements to large_list
            else:
                count_pivot += 1  # Count occurrences of the pivot
        
        # Append the pivot element(s) to small_list
        for i in range(count_pivot):
            small_list.append(pivot)
        
        # Concatenate smaller elements, pivot elements, and larger elements
        return small_list + large_list

