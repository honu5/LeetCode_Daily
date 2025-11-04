class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Find the x-sum for each sliding window of size k.
        The x-sum is the sum of the top x most frequent elements (frequency * value).
      
        Args:
            nums: Input array of integers
            k: Size of the sliding window
            x: Number of top frequent elements to consider
          
        Returns:
            List of x-sums for each window
        """
      
        def add_element_to_sets(value: int) -> None:
            """Add an element to either top_x_elements or remaining_elements based on priority."""
            if element_count[value] == 0:
                return
          
            priority_tuple = (element_count[value], value)
          
            if top_x_elements and priority_tuple > top_x_elements[0]:
                nonlocal current_sum
                current_sum += priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_elements.add(priority_tuple)
            else:
                remaining_elements.add(priority_tuple)
      
        def remove_element_from_sets(value: int) -> None:
            """Remove an element from either top_x_elements or remaining_elements."""
            if element_count[value] == 0:
                return
          
            priority_tuple = (element_count[value], value)
          
            if priority_tuple in top_x_elements:
                nonlocal current_sum
                current_sum -= priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_elements.remove(priority_tuple)
            else:
                remaining_elements.remove(priority_tuple)
      
        top_x_elements = SortedList()      # Stores top x frequent elements
        remaining_elements = SortedList()   # Stores remaining elements
        element_count = Counter()           # Tracks frequency of each element
        current_sum = 0                     # Current x-sum
        n = len(nums)
        result = [0] * (n - k + 1)         # Result array for all windows
      
        for i, current_value in enumerate(nums):
            remove_element_from_sets(current_value)
            element_count[current_value] += 1
            add_element_to_sets(current_value)
          
            window_start = i - k + 1
          
            if window_start < 0:
                continue
          
            
            while remaining_elements and len(top_x_elements) < x:
                element_to_promote = remaining_elements.pop()
                top_x_elements.add(element_to_promote)
                current_sum += element_to_promote[0] * element_to_promote[1]
          
            while len(top_x_elements) > x:
                element_to_demote = top_x_elements.pop(0)
                current_sum -= element_to_demote[0] * element_to_demote[1]
                remaining_elements.add(element_to_demote)
          
            result[window_start] = current_sum
          
            leftmost_element = nums[window_start]
            remove_element_from_sets(leftmost_element)
            element_count[leftmost_element] -= 1
            if element_count[leftmost_element] > 0:
                add_element_to_sets(leftmost_element)
      
        return result
