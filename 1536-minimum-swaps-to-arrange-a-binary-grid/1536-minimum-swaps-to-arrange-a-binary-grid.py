class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = list(map(lambda r: (r[::-1] + [1]).index(1), grid))
        
        swaps = 0
        for i in range(n):
            j = (zeros + [n]).index(next(filter(lambda v: v >= n - 1 - i, zeros + [n])))
            if j == len(zeros): return -1
            swaps += j
            zeros.pop(j)
        return swaps