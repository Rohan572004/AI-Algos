import random

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distances[route[i]][route[(i + 1) % len(route)]]
    return total_distance

def get_neighbors(route):
    neighbors = []
    for i in range(len(route) - 1):
        for j in range(i + 1, len(route)):
            # Swap two cities to create a new neighbor
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing_tsp(distances):
    # Initial random solution (random order of cities)
    route = list(range(len(distances)))
    random.shuffle(route)

    current_distance = calculate_distance(route, distances)
    best_route = route[:]
    best_distance = current_distance

    print(f"Initial route: {route}, Distance: {best_distance}")

    while True:
        neighbors = get_neighbors(best_route)
        neighbor_distances = [(calculate_distance(neighbor, distances), neighbor) for neighbor in neighbors]
        
        # Find the neighbor with the shortest distance
        neighbor_distance, neighbor_route = min(neighbor_distances, key=lambda x: x[0])

        if neighbor_distance < best_distance:
            best_route = neighbor_route
            best_distance = neighbor_distance
            print(f"New best route: {best_route}, Distance: {best_distance}")
        else:
            # No better neighbors, so break out of the loop
            break

    return best_route, best_distance

# Example distance matrix (symmetric TSP with 5 cities)
distances = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]

# Running the hill climbing TSP
best_route, best_distance = hill_climbing_tsp(distances)
print(f"Final best route: {best_route}, Distance: {best_distance}")
