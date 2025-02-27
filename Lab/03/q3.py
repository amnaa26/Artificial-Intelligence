class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_value, to_value):
        if from_value in self.nodes and to_value in self.nodes:
            self.nodes[from_value].children.append(self.nodes[to_value])

class IDDFSAgent:
    def __init__(self, goal):
        self.goal = goal

    def dls(self, node, goal, depth):
        if depth == 0 and node.value == goal:
            return [node.value]
        if depth > 0:
            for child in node.children:
                result = self.dls(child, goal, depth - 1)
                if result:
                    return [node.value] + result
        return None

    def iddfs(self, start_node, goal):
        depth = 0
        while True:
            result = self.dls(start_node, goal, depth)
            if result:
                return result
            depth += 1

class BidirectionalSearchAgent:
    def __init__(self, goal):
        self.goal = goal

    def bidirectional_search(self, start_node, goal_node):
        from collections import deque

        forward_queue = deque([(start_node, [start_node.value])])
        backward_queue = deque([(goal_node, [goal_node.value])])

        forward_visited = {start_node.value: [start_node.value]}
        backward_visited = {goal_node.value: [goal_node.value]}

        while forward_queue and backward_queue:
            # Forward search
            current_forward, path_forward = forward_queue.popleft()
            if current_forward.value in backward_visited:
                return path_forward + backward_visited[current_forward.value][::-1][1:]

            for child in current_forward.children:
                if child.value not in forward_visited:
                    forward_visited[child.value] = path_forward + [child.value]
                    forward_queue.append((child, path_forward + [child.value]))

            # Backward search
            current_backward, path_backward = backward_queue.popleft()
            if current_backward.value in forward_visited:
                return forward_visited[current_backward.value] + path_backward[::-1][1:]

            for parent in [n for n in graph.nodes.values() if current_backward in n.children]:
                if parent.value not in backward_visited:
                    backward_visited[parent.value] = path_backward + [parent.value]
                    backward_queue.append((parent, path_backward + [parent.value]))

        return None


graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'F')

start_node = graph.nodes['A']
goal_node = graph.nodes['F']

# IDDFS Agent
iddfs_agent = IDDFSAgent('F')
iddfs_result = iddfs_agent.iddfs(start_node, 'F')
print(f"IDDFS Path: {iddfs_result}")

# Bidirectional Search Agent
bidirectional_agent = BidirectionalSearchAgent('F')
bidirectional_result = bidirectional_agent.bidirectional_search(start_node, goal_node)
print(f"Bidirectional Search Path: {bidirectional_result}")