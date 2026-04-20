class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        val=-1
        for i in range(n):
            for j in range(1,n):
                if colors[i]!=colors[j]:
                    val=max(abs(i-j),val)
        return val
                    
        