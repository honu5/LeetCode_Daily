class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if len(str(i))==1:
                ans.append(i)
            else:
                for j in str(i):
                    ans.append(int(j))
        return ans