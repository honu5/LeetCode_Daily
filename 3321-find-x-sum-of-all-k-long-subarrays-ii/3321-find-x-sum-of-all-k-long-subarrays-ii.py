class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Find the sum of top x frequent elements for each sliding window of size k.
        Elements are ranked by (frequency, value) in descending order.
      
        Args:
            nums: Input array
            k: Window size
            x: Number of top frequent elements to sum
      
        Returns:
            List of sums for each window
        """
      
        def add_to_sets(value: int) -> None:
            """Add element to either top_x_set or remaining_set based on its priority."""
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            # If top_x_set is empty or this element has higher priority than the minimum in top_x_set
            if top_x_set and priority_tuple > top_x_set[0]:
                nonlocal current_sum
                current_sum += priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.add(priority_tuple)
            else:
                remaining_set.add(priority_tuple)
      
        def remove_from_sets(value: int) -> None:
            """Remove element from whichever set it belongs to."""
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            if priority_tuple in top_x_set:
                nonlocal current_sum
                current_sum -= priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.remove(priority_tuple)
            else:
                remaining_set.remove(priority_tuple)
      
        # Initialize data structures
        top_x_set = SortedList()      # Maintains top x elements by (frequency, value)
        remaining_set = SortedList()   # Maintains remaining elements
        frequency_map = Counter()       # Tracks frequency of each element in current window
        current_sum = 0                 # Sum of top x elements
        n = len(nums)
        result = [0] * (n - k + 1)     # Result array for each window
      
        # Process each element
        for i, current_value in enumerate(nums):
            # Update frequency for current element
            remove_from_sets(current_value)
            frequency_map[current_value] += 1
            add_to_sets(current_value)
          
            # Calculate window start index
            window_start = i - k + 1
          
            # Skip if we haven't formed a complete window yet
            if window_start < 0:
                continue
          
            # Balance the sets: ensure top_x_set has exactly x elements
            # Move elements from remaining_set to top_x_set if needed
            while remaining_set and len(top_x_set) < x:
                element = remaining_set.pop()
                top_x_set.add(element)
                current_sum += element[0] * element[1]
          
            # Move excess elements from top_x_set to remaining_set
            while len(top_x_set) > x:
                element = top_x_set.pop(0)  # Remove smallest element
                current_sum -= element[0] * element[1]
                remaining_set.add(element)
          
            # Store result for current window
            result[window_start] = current_sum
          
            # Remove the leftmost element of the window for next iteration
            leftmost_element = nums[window_start]
            remove_from_sets(leftmost_element)
            frequency_map[leftmost_element] -= 1
            if frequency_map[leftmost_element] > 0:
                add_to_sets(leftmost_element)
      
        return result