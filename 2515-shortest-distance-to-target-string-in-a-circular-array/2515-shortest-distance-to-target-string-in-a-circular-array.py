class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        n2=n//2+1
        for d in range(n2):
            l=startIndex-d if startIndex>=d else n+startIndex-d
            r=startIndex+d-n if startIndex+d>=n else startIndex+d
            if words[l]==target or words[r]==target: return d
        return -1