from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # dist[r][c] will store the minimum health points lost to reach (r, c)
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting point
        dist[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the destination, we can early exit if we want, 
            # but standard 0-1 BFS will find it optimally anyway.
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    
                    # If a shorter path to (nr, nc) is found
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        
                        # 0-1 BFS optimization: 
                        # 0 weight goes to the front, 1 weight goes to the back
                        if weight == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        # The remaining health must be at least 1
        return health - dist[m - 1][n - 1] >= 1