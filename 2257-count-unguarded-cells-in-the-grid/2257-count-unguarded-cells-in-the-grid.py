class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0] * n for _ in range(m)]
      
        for row, col in guards:
            grid[row][col] = 2
      
        for row, col in walls:
            grid[row][col] = 2
      
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      
        for guard_row, guard_col in guards:
            for delta_row, delta_col in directions:
                current_row, current_col = guard_row, guard_col
              
                while (0 <= current_row + delta_row < m and 
                       0 <= current_col + delta_col < n and 
                       grid[current_row + delta_row][current_col + delta_col] < 2):
                    current_row += delta_row
                    current_col += delta_col
                    grid[current_row][current_col] = 1  
      
        unguarded_count = sum(cell == 0 for row in grid for cell in row)
      
        return unguarded_count

        