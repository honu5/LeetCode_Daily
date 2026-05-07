class Solution:
    def maxValue(self, a: List[int]) -> List[int]:
        b = zip([*accumulate(a,max)][::-1],accumulate([inf]+a[::-1],min))
        return [*accumulate(b,lambda q,p:p[0]>p[1] and q or p[0],initial=0)][:0:-1]