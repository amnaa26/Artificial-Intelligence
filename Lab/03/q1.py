# Base Goal-Based Agent
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return environment.search(percept, self.goal, self.search_type)

# Environment Class
class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def search(self, start, goal, search_type):
        if search_type == "DFS":
            return self.dfs_search(start, goal)
        elif search_type == "DLS":
            return self.dls_search(start, goal, depth_limit=2)  # Example depth limit
        elif search_type == "UCS":
            return self.ucs_search(start, goal)
        else:
            return "Invalid search type"

    def dfs_search(self, start, goal):
        visited = set()
        stack = [(start, [start])]  # Stack of (node, path)

        while stack:
            node, path = stack.pop()
            if node == goal:
                return f"Goal {goal} found! Path: {path}"
            if node not in visited:
                visited.add(node)
                for neighbour in reversed(self.graph.get(node, [])):  # Reverse to maintain order
                    if neighbour not in visited:
                        stack.append((neighbour, path + [neighbour]))
        return "Goal not found"

    def dls_search(self, start, goal, depth_limit):
        def recursive_dls(node, goal, depth):
            if depth == 0:
                return None
            if node == goal:
                return [node]
            for neighbour in self.graph.get(node, []):
                result = recursive_dls(neighbour, goal, depth - 1)
                if result is not None:
                    return [node] + result
            return None

        result = recursive_dls(start, goal, depth_limit)
        if result:
            return f"Goal {goal} found! Path: {result}"
        else:
            return "Goal not found within depth limit"

    def ucs_search(self, start, goal):
        from queue import PriorityQueue
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, start, [start]))  # (cost, node, path)

        while not priority_queue.empty():
            cost, node, path = priority_queue.get()
            if node == goal:
                return f"Goal {goal} found! Path: {path}, Cost: {cost}"
            if node not in visited:
                visited.add(node)
                for neighbour, edge_cost in self.graph.get(node, {}).items():
                    if neighbour not in visited:
                        priority_queue.put((cost + edge_cost, neighbour, path + [neighbour]))
        return "Goal not found"

# Utility-Based Agent for UCS
class UtilityBasedAgent(GoalBasedAgent):
    def __init__(self, goal):
        super().__init__(goal)
        self.search_type = "UCS"

# Tree Representation with Edge Costs (for UCS)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3, 'G': 6},
    'D': {'H': 7},
    'E': {},
    'F': {'I': 8},
    'G': {},
    'H': {},
    'I': {}
}

# Helper function to run the agent
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)


# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Create instances of agents and environment
dfs_agent = GoalBasedAgent(goal_node)
dfs_agent.search_type = "DFS"

dls_agent = GoalBasedAgent(goal_node)
dls_agent.search_type = "DLS"

ucs_agent = UtilityBasedAgent(goal_node)

environment = Environment(graph)

# Run the agents
print("DFS Agent:")
run_agent(dfs_agent, environment, start_node)

print("\nDLS Agent:")
run_agent(dls_agent, environment, start_node)

print("\nUCS Agent:")
run_agent(ucs_agent, environment, start_node)