import heapq


class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    # Goal test
    def goalTest(self, state):
        return state == self.goal_state

    # Find blank position
    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    # Successor function
    def successor(self, state):
        successors = []
        x, y = self.find_blank(state)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                successors.append(tuple(tuple(row) for row in new_state))

        return successors

    # Manhattan distance heuristic
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

    # A* Algorithm
    def a_star(self):
        OPEN = []
        heapq.heappush(OPEN, (0, self.initial_state))
        CLOSED = {self.initial_state: None}
        g_cost = {self.initial_state: 0}

        while OPEN:
            _, current = heapq.heappop(OPEN)

            if self.goalTest(current):
                return self.generate_path(CLOSED, current)

            for child in self.successor(current):
                new_g = g_cost[current] + 1

                if child not in g_cost or new_g < g_cost[child]:
                    g_cost[child] = new_g
                    f = new_g + self.heuristic(child)
                    heapq.heappush(OPEN, (f, child))
                    CLOSED[child] = current

        return None

    # Generate solution path
    def generate_path(self, CLOSED, goal):
        path = []
        while goal is not None:
            path.append(goal)
            goal = CLOSED[goal]
        return path[::-1]


# Driver Code
initial_state = ((1, 2, 3), (4, 0, 6), (7, 5, 8))

goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

puzzle = EightPuzzle(initial_state, goal_state)
solution = puzzle.a_star()

print("Solution Path:")
for step in solution:
    for row in step:
        print(row)
    print()
