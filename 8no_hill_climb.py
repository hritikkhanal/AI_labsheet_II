class HillClimbing8Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    # Find blank tile
    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    # Generate successors
    def successor(self, state):
        x, y = self.find_blank(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        successors = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                successors.append(tuple(tuple(row) for row in new_state))

        return successors

    # Manhattan Distance Heuristic
    def heuristic(self, state):
        h = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    for x in range(3):
                        for y in range(3):
                            if self.goal_state[x][y] == value:
                                h += abs(i - x) + abs(j - y)
        return h

    # Steepest Ascent Hill Climbing
    def steepest_ascent(self):
        current = self.initial_state
        path = [current]

        while True:
            current_h = self.heuristic(current)
            neighbors = self.successor(current)

            best_neighbor = current
            best_h = current_h

            for n in neighbors:
                h = self.heuristic(n)
                if h < best_h:
                    best_h = h
                    best_neighbor = n

            if best_h >= current_h:
                # No improvement → stuck
                return path

            current = best_neighbor
            path.append(current)

    # Display board
    def display(self, state):
        for row in state:
            print(row)
        print()


# Driver Code
initial_state = ((1, 2, 3), (4, 0, 6), (7, 5, 8))

goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

hc = HillClimbing8Puzzle(initial_state, goal_state)
solution_path = hc.steepest_ascent()

print("Path followed:")
for step in solution_path:
    hc.display(step)

print("Final heuristic value:", hc.heuristic(solution_path[-1]))
