class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visit = [False] * (m * n)
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def dfs(r, c, pr, pc):
            visit[r * n + c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (nr, nc) != (pr, pc):
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == grid[r][c]:
                            if visit[nr * n + nc] or dfs(nr, nc, r, c):
                                return True

            return False

        return any(not visit[i] and dfs(i // n, i % n, -1, -1) for i in range(m * n))