class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        answer = [-1] * n

        for pos in positions.values():
            m = len(pos)

            if m == 1:
                continue

            for i in range(m):
                curr = pos[i]

                prev_idx = pos[(i - 1 + m) % m]
                next_idx = pos[(i + 1) % m]

                dist_prev = abs(curr - prev_idx)
                dist_prev = min(dist_prev, n - dist_prev)

                dist_next = abs(curr - next_idx)
                dist_next = min(dist_next, n - dist_next)

                answer[curr] = min(dist_prev, dist_next)

        return [answer[idx] for idx in queries]