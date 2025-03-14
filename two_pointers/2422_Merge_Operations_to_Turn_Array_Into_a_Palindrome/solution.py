
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Initialize two pointers for the start and end of the list
        left_index, right_index = 0, len(nums) - 1

        # Initialize the sums of elements from the start and from the end
        left_sum, right_sum = nums[left_index], nums[right_index]

        # Initialize a variable to count the number of operations performed
        operations_count = 0

        # Loop until the two pointers meet or cross each other
        while left_index < right_index:

            # If the sum on the left is less than the sum on the right,
            # move the left pointer to the right and add the new element to left_sum
            if left_sum < right_sum:
                left_index += 1
                left_sum += nums[left_index]
                operations_count += 1
            # If the sum on the right is less than the sum on the left,
            # move the right pointer to the left and add the new element to right_sum
            elif right_sum < left_sum:
                right_index -= 1
                right_sum += nums[right_index]
                operations_count += 1
            # If the sums are equal, move both pointers and update the sums
            else:
                left_index += 1
                right_index -= 1
                # Check if pointers are still within the array bounds
                if left_index < right_index:
                    left_sum = nums[left_index]
                    right_sum = nums[right_index]

        # Return the total number of operations to make segments equal
        return operations_count
