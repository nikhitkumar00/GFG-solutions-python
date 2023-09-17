class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        queue = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == rows or
                        col < 0 or col == cols) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1


n, m = map(int, input().split())
grid = []
obj = Solution()
ans = obj.orangesRotting(grid)
print(ans)
