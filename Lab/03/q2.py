class TSPAgent:
    def __init__(self, cities, distance_matrix):
        self.cities = cities
        self.distance_matrix = distance_matrix

    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        total_distance += self.distance_matrix[route[-1]][route[0]]  # Return to the starting city
        return total_distance

    def generate_permutations(self, cities):
        if len(cities) <= 1:
            return [cities]
        permutations = []
        for i in range(len(cities)):
            first_city = cities[i]
            remaining_cities = cities[:i] + cities[i + 1:]
            for p in self.generate_permutations(remaining_cities):
                permutations.append([first_city] + p)
        return permutations

    def find_shortest_route(self):
        shortest_route = None
        min_distance = float('inf')

        # Generating all possible routes
        all_routes = self.generate_permutations(self.cities)
        for route in all_routes:
            current_distance = self.calculate_total_distance(route)
            if current_distance < min_distance:
                min_distance = current_distance
                shortest_route = route

        return shortest_route, min_distance

# Distance matrix representing the distances between cities
distance_matrix = {
    1: {1: 0, 2: 10, 3: 15, 4: 20},
    2: {1: 10, 2: 0, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 3: 0, 4: 30},
    4: {1: 20, 2: 25, 3: 30, 4: 0}
}

# List of cities
cities = [1, 2, 3, 4]

# Create an instance of the TSPAgent
tsp_agent = TSPAgent(cities, distance_matrix)

# Finding the shortest route
shortest_route, min_distance = tsp_agent.find_shortest_route()

# Output the result
print(f"Shortest Route: {shortest_route}")
print(f"Minimum Distance: {min_distance}")