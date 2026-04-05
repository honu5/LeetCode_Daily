class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) & 1: return False
        x = y = 0

        for c in moves:
            y += (c == 'U') - (c == 'D')
            x += (c == 'R') - (c == 'L')

        return not x and not y