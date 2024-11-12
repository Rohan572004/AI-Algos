from collections import deque

# BFS Algorithm Implementation
def bfs(graph, start, target):
    visited = set()  # Set to store visited nodes
    queue = deque([start])  # Queue to store nodes to visit

    visited.add(start)

    while queue:
        node = queue.popleft()  # Remove the front node from the queue

        print(f"Visiting node: {node}")

        if node == target:
            print(f"Target node {target} found!")
            return True

        # Check all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Add the neighbor to the queue

    print("Target node not found!")
    return False


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call BFS
start_node = 'A'
target_node = 'F'
bfs(graph, start_node, target_node)
