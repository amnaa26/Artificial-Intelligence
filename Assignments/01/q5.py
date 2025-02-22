romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

heuristics = {
    'Arad': 366, 
    'Bucharest': 0, 
    'Craiova': 160, 
    'Drobeta': 242,
    'Eforie': 161, 
    'Fagaras': 176, 
    'Giurgiu': 77, 
    'Hirsova': 151,
    'Iasi': 226, 
    'Lugoj': 244, 
    'Mehadia': 241, 
    'Neamt': 234,
    'Oradea': 380, 
    'Pitesti': 100, 
    'Rimnicu Vilcea': 193,
    'Sibiu': 253, 
    'Timisoara': 329, 
    'Urziceni': 80,
    'Vaslui': 199, 
    'Zerind': 374
}

''' Uniform-cost search '''
def ucs(graph, start, goal):
    queue = [(0, start, [start])] #queue will store tuples of form (cost, current_node, path_to_current_node)
    visited = set()
    while queue:
        queue.sort() #queue is sorted in ascending order i.e we will first explore the node with lowest cost
        cost, next, path = queue.pop(0) #removes the first tuple present in the queue and unpacks it into three variables i.e cost, next and path
        if next == goal:
            return path, cost
        
        if next not in visited:
            visited.add(next)
            for neighbor, cost_edge in graph[next].items(): #exploring the neighbors of current_node
                if neighbor not in visited: #checking if neighbouring node is already c=visited
                    queue.append((cost + cost_edge, neighbor, path + [neighbor])) #cost+cost-edge --> total cost to reach the neighbor node
    return None, float('inf')  # No path found


''' Breadth-first search '''
def bfs(graph, start, goal):
    #queue will store tuples of form (current_node, path_to_current_node)
    queue = [(start, [start])] 
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0) #removes the first element present in the queue and store it in vertex and path
        if vertex == goal:
                return path
        
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor])) #next node is added to queue so that we will explore it in the while loop
    return None


''' Greedy Best First search '''
def gbfs(graph, start, goal, heuristic):
    #queue will store tuples of form (heuristic, current_node, path)
    queue = [(heuristic[start], start, [start])] #queue stores the heuristic value of starting node(heuristic[start]), current_node and path taken to the current_node
    visited = set()
    while queue:
        queue.sort() #sorting by heuristic value (ascending order)
        h, vertex, path = queue.pop(0)
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]: #exploring the neighbors of current node
                if neighbor not in visited:
                    queue.append((heuristic[neighbor], neighbor, path + [neighbor]))
    return None


''' Iterative deepening depth first search '''
def iddfs(graph, start, goal, max_depth):
    #this loop will perfrom dls(depth limited search) at each depth level
    for depth in range(max_depth): 
        result = dls(graph, start, goal, depth)
        if result is not None: #goal is found
            return result
    return None

def dls(graph, start, goal, limit):
    #base case for recursion
    if start == goal:
        return [start]
    
    #checks if depth limit has reached i.e 0 or -ve 
    #if limit <= 0 it means the goal state was not found in the duration of this depth limit
    if limit <= 0:
        return None 
    
    for next in graph[start]:
        result = dls(graph, next, goal, limit - 1)
        if result is not None: #goal found
            return [start] + result #returns the path from start to goal by adding result
    return None


start = input("Enter start node: ").strip() #.strip() removes any leading/trailing whitespace
goal = input( "Enter goal node: ").strip()

#checking if user has entered the node which exists in graph
if start not in romania_map or goal not in romania_map:
    print("Invalid start or goal node.")

else:
    # BFS
    bfs_path = bfs(romania_map, start, goal)
    '''
    if bfs_path --> checks if the path exists? 
    else float('inf') --> sets cost to infinity if path does not exists

    cost is calculated by summing the edge weights between consecutive nodes in the path.
    '''
    bfs_cost = sum(romania_map[bfs_path[i]][bfs_path[i+1]] for i in range(len(bfs_path)-1)) if bfs_path else float('inf')

    # UCS
    ucs_path, ucs_cost = ucs(romania_map, start, goal)

    # GBFS
    gbfs_path = gbfs(romania_map, start, goal, heuristics)
    gbfs_cost = sum(romania_map[gbfs_path[i]][gbfs_path[i+1]] for i in range(len(gbfs_path)-1)) if gbfs_path else float('inf')

    # IDDFS
    iddfs_path = iddfs(romania_map, start, goal, 20)
    iddfs_cost = sum(romania_map[iddfs_path[i]][iddfs_path[i+1]] for i in range(len(iddfs_path)-1)) if iddfs_path else float('inf')

    # Results
    results = {
        'BFS': {'Path': bfs_path, 'Cost': bfs_cost},
        'UCS': {'Path': ucs_path, 'Cost': ucs_cost},
        'GBFS': {'Path': gbfs_path, 'Cost': gbfs_cost},
        'IDDFS': {'Path': iddfs_path, 'Cost': iddfs_cost}
    }

    # Sort by cost
    sorted_results = sorted(results.items(), key=lambda x: x[1]['Cost'])

    for algorithm, data in sorted_results:
        print(f"{algorithm}: Path = {data['Path']}, Cost = {data['Cost']}")