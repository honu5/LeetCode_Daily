class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[]
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[k] and nums[k]==nums[j]:
                        ans.append([i,j,k])
                        break
        if not ans:
            return -1
        val=float("inf")
        for i in ans:
            vals=abs(i[0]-i[1])+abs(i[0]-i[2])+abs(i[1]-i[2])
            val=min(vals,val)
        return val
        