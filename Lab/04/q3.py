import heapq

# Grid setup
maze = [
    ["S", ".", ".", "D1", "#"],
    [".", "#", ".", ".", "."],
    [".", ".", ".", "#", "D2"],
    ["D3", ".", "#", ".", "."],
    [".", "D4", ".", ".", "."],
]

# Destination info: name → (row, col, start_time, end_time)
destinations = {
    "D1": (0, 3, 5, 15),
    "D2": (2, 4, 8, 12),
    "D3": (3, 0, 10, 20),
    "D4": (4, 1, 7, 14),
}

# Starting point
origin = (0, 0)

# Manhattan distance
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Greedy Best-First Search
def find_path(grid, start, goals):
    visited = set()
    path = []
    time = 0
    queue = []
    heapq.heappush(queue, (0, start, time))

    while queue:
        _, curr, time = heapq.heappop(queue)
        if curr in visited:
            continue
        visited.add(curr)
        path.append(curr)

        # If current position is a destination and within allowed time
        to_remove = None
        for label, (gx, gy, t1, t2) in goals.items():
            if (gx, gy) == curr and t1 <= time <= t2:
                to_remove = label
                break
        if to_remove:
            goals.pop(to_remove)

        # Explore neighbors
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = curr[0] + dx, curr[1] + dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                continue
            if grid[nx][ny] == "#" or (nx, ny) in visited:
                continue

            # Heuristic: choose direction closer to any reachable goal in time
            best_cost = float('inf')
            for gx, gy, start_t, end_t in goals.values():
                est_time = time + 1 + manhattan((nx, ny), (gx, gy))
                if est_time <= end_t:
                    score = manhattan((nx, ny), (gx, gy))
                    if score < best_cost:
                        best_cost = score
            heapq.heappush(queue, (best_cost, (nx, ny), time + 1))

    return path

# Run search
route_taken = find_path(maze, origin, dict(destinations))
print("Path visited:", route_taken)
