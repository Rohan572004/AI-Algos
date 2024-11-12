from collections import deque

class State:
    def __init__(self, jugA, jugB, path):
        self.jugA = jugA
        self.jugB = jugB
        self.path = path

    def __str__(self):
        return f"({self.jugA}, {self.jugB})"


def solve_water_jug_problem(capacityA, capacityB, target):
    # Initialize the queue and visited set
    queue = deque([State(0, 0, "Start")])
    visited = set((0, 0))

    while queue:
        current = queue.popleft()

        # Check if we reached the goal state
        if (current.jugA == target and current.jugB == 0) or (current.jugA == 0 and current.jugB == target):
            print(f"Solution found: {current.path} -> {current}")
            return

        # Generate possible next states and add to the queue
        next_states = [
            (capacityA, current.jugB, "Fill A"),  # Fill Jug A
            (current.jugA, capacityB, "Fill B"),  # Fill Jug B
            (0, current.jugB, "Empty A"),         # Empty Jug A
            (current.jugA, 0, "Empty B"),         # Empty Jug B
            # Pour from Jug A to Jug B
            (max(current.jugA - (capacityB - current.jugB), 0), min(capacityB, current.jugA + current.jugB), "Pour A to B"),
            # Pour from Jug B to Jug A
            (min(capacityA, current.jugA + current.jugB), max(current.jugB - (capacityA - current.jugA), 0), "Pour B to A")
        ]

        for jugA, jugB, action in next_states:
            if (jugA, jugB) not in visited:
                queue.append(State(jugA, jugB, current.path + f" -> {action}"))
                visited.add((jugA, jugB))

    print("No solution found.")


# Usage
solve_water_jug_problem(4, 3, 2)
