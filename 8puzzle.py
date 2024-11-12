import heapq

class PuzzleState:
    def __init__(self, board, g, h, parent=None):
        self.board = board
        self.g = g  # Cost to reach this state
        self.h = h  # Heuristic estimate to goal
        self.parent = parent

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))


def print_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    for step in path[::-1]:
        print_board(step)
    print()


def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()


def get_goal_position(value):
    """Return the goal position of a tile in a 3x3 grid."""
    return divmod(value - 1, 3)


def manhattan_distance(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                goal_i, goal_j = get_goal_position(value)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance


def get_neighbors(state):
    board = state.board
    neighbors = []
    blank_row, blank_col = next((r, c) for r in range(3) for c in range(3) if board[r][c] == 0)

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Swap blank with neighbor
            new_board = [row[:] for row in board]
            new_board[blank_row][blank_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_row][blank_col]
            neighbors.append(new_board)
    return neighbors


def a_star_search(start, goal):
    open_list = []
    closed_set = set()
    start_h = manhattan_distance(start, goal)
    start_state = PuzzleState(start, g=0, h=start_h)

    heapq.heappush(open_list, (start_state.g + start_state.h, start_state))

    while open_list:
        _, current_state = heapq.heappop(open_list)

        if current_state.board == goal:
            print("Solution found!")
            print_path(current_state)
            return

        closed_set.add(current_state)

        for neighbor_board in get_neighbors(current_state):
            neighbor_g = current_state.g + 1
            neighbor_h = manhattan_distance(neighbor_board, goal)
            neighbor_state = PuzzleState(neighbor_board, neighbor_g, neighbor_h, current_state)

            if neighbor_state in closed_set:
                continue

            heapq.heappush(open_list, (neighbor_state.g + neighbor_state.h, neighbor_state))

    print("No solution found.")
    return None


# Starting and Goal State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

a_star_search(start, goal)
