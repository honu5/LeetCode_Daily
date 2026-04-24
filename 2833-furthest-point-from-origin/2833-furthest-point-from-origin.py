class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n=len(moves)
        Ls=moves.count("L")
        Rs=moves.count("R")
        other=n-(Ls+Rs)
        return max(Ls,Rs)-min(Ls,Rs)+other
        