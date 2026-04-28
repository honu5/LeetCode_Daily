class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[i for row in grid for i in row]
        b=grid[0][0]%x
        for i in arr:
            if i%x!=b:
                return -1
        arr.sort()
        med=arr[len(arr)//2]
        a=0
        for i in arr:
            a+=(abs(i-med)//x)
        return a

        