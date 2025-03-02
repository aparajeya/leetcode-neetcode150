from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:       
        # Initialize pointers for both input arrays
        first_array_index = 0
        second_array_index = 0
        final_list = []  # List to store the merged output

        # Traverse both arrays while there are elements in both
        while first_array_index < len(nums1) and second_array_index < len(nums2):
            # If the ID in nums1 is smaller, add it to the final list and move the pointer
            if nums1[first_array_index][0] < nums2[second_array_index][0]:
                final_list.append(nums1[first_array_index])
                first_array_index += 1

            # If the ID in nums2 is smaller, add it to the final list and move the pointer
            elif nums1[first_array_index][0] > nums2[second_array_index][0]:
                final_list.append(nums2[second_array_index])
                second_array_index += 1

            # If IDs are equal, sum their values and add the merged entry to the final list
            else: 
                index = nums1[first_array_index][0]  # Common index
                num_sum = nums1[first_array_index][1] + nums2[second_array_index][1]  # Summing values
                temp_arr = [index, num_sum]  # Create a merged entry
                final_list.append(temp_arr)  # Add to final list
                
                # Move both pointers forward
                first_array_index += 1
                second_array_index += 1

        # If there are remaining elements in nums1, add them to the final list
        while first_array_index < len(nums1):
            final_list.append(nums1[first_array_index])
            first_array_index += 1

        # If there are remaining elements in nums2, add them to the final list
        while second_array_index < len(nums2):
            final_list.append(nums2[second_array_index])
            second_array_index += 1
        
        # Return the merged sorted list
        return final_list
