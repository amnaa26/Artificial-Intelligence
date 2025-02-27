import random

class AStar:
    def __init__(self, grid):
        self.grid = grid

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, position):
        x, y = position
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] != 1:
                neighbors.append((nx, ny))
        return neighbors

    def a_star(self, start, goal):
        open_set = [(0, start)]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            open_set.sort()
            _, current = open_set.pop(0)
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1  # Assuming uniform cost
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    open_set.append((f_score[neighbor], neighbor))

            # Simulate dynamic cost changes
            if random.random() < 0.1:  # 10% chance to change edge costs
                self.grid[random.randint(0, len(self.grid)-1)][random.randint(0, len(self.grid[0])-1)] = random.randint(0, 1)

        return None


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
a_star = AStar(grid)
start = (0, 0)
goal = (4, 4)
path = a_star.a_star(start, goal)
print(f"A* Path: {path}")