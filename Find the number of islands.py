# User function Template for python3
from collections import deque

class Solution:
    def numIslands(self, grid):

        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(row, col):
            q = deque()

            q.append((row, col))
            visited.add((row, col))

            directions = (
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
                (1, 1),
                (1, -1),
                (-1, -1),
                (-1, 1),
            )

            while q:

                r, c = q.popleft()
                for dr, dc in directions:

                    nr, nc = dr + r, dc + c

                    if (
                        nr in range(rows)
                        and nc in range(cols)
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

if __name__ == "__main__":
    grid = [
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    ]
    obj = Solution()
    print(obj.numIslands(grid))
# } Driver Code Ends
