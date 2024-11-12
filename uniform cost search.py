import heapq

# Uniform Cost Search function
def uniform_cost_search(graph, start, goal):
    # Priority queue to store (cost, node, path)
    priority_queue = [(0, start, [start])]
    visited = set()  # Track visited nodes

    while priority_queue:
        # Pop the node with the lowest cost
        current_cost, current_node, path = heapq.heappop(priority_queue)

        # Goal check
        if current_node == goal:
            return current_cost, path  # Return the cost and the path

        # If the node has been visited, skip it
        if current_node in visited:
            continue
        visited.add(current_node)

        # Expand the current node and add neighbors to the queue
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                total_cost = current_cost + cost
                heapq.heappush(priority_queue, (total_cost, neighbor, path + [neighbor]))

    return float('inf'), []  # Return if no path found


# Example graph represented as an adjacency list with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Run Uniform Cost Search from 'A' to 'D'
start_node = 'A'
goal_node = 'D'
cost, path = uniform_cost_search(graph, start_node, goal_node)

print(f"Minimum cost from {start_node} to {goal_node} is {cost}")
print(f"Path: {' -> '.join(path)}")
