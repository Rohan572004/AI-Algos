# Recursive DFS function
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the node as visited
    visited.add(node)
    print(node, end=" ")  # Process the node (for example, print it)

    # Recurse for all the adjacent nodes
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting the DFS traversal from node 'A'
dfs_recursive(graph, 'A')
