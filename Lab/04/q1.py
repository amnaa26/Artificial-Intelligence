class Maze:
    def __init__(self, grid, goals):
        self.grid = grid
        self.goals = goals

    def get_neighbors(self, position):
        x, y = position
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] != 1:
                neighbors.append((nx, ny))
        return neighbors

def best_first_search(maze, start):
    queue = [(start, [start])]
    visited = set()
    goals_remaining = set(maze.goals)

    while queue:
        current, path = queue.pop(0)
        if current in goals_remaining:
            goals_remaining.remove(current)
            if not goals_remaining:
                return path
        visited.add(current)
        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
goals = [(4, 4), (2, 2), (0, 4)]
maze = Maze(grid, goals)
start = (0, 0)
path = best_first_search(maze, start)
print(f"Path covering all goals: {path}")