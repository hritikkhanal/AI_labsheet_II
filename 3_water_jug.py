from collections import deque


class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    # Goal test function
    def goalTest(self, current_state):
        return current_state[0] == self.goal_state[0]

    # Successor function using production rules
    def successor(self, state):
        x, y = state
        successors = []

        # Capacities
        max_x = 4
        max_y = 3

        # 1. Fill 4-liter jug
        successors.append((max_x, y))

        # 2. Fill 3-liter jug
        successors.append((x, max_y))

        # 3. Empty 4-liter jug
        successors.append((0, y))

        # 4. Empty 3-liter jug
        successors.append((x, 0))

        # 5. Pour 4 → 3
        transfer = min(x, max_y - y)
        successors.append((x - transfer, y + transfer))

        # 6. Pour 3 → 4
        transfer = min(y, max_x - x)
        successors.append((x + transfer, y - transfer))

        return successors

    # Verify successor function
    def verify_successor(self):
        print("Successors of initial state:")
        for s in self.successor(self.initial_state):
            print(s)

    # BFS Search
    def bfs(self):
        OPEN = deque([self.initial_state])
        CLOSED = {self.initial_state: None}

        while OPEN:
            current = OPEN.popleft()

            if self.goalTest(current):
                return self.generate_path(CLOSED, current)

            for child in self.successor(current):
                if child not in CLOSED:
                    OPEN.append(child)
                    CLOSED[child] = current

        return None

    # DFS Search
    def dfs(self):
        OPEN = [self.initial_state]
        CLOSED = {self.initial_state: None}

        while OPEN:
            current = OPEN.pop()

            if self.goalTest(current):
                return self.generate_path(CLOSED, current)

            for child in self.successor(current):
                if child not in CLOSED:
                    OPEN.append(child)
                    CLOSED[child] = current

        return None

    # Generate solution path
    def generate_path(self, CLOSED, goal_state):
        path = []
        while goal_state is not None:
            path.append(goal_state)
            goal_state = CLOSED[goal_state]
        return path[::-1]


# Driver Code
initial = (4, 0)
goal = (2, 0)

jug = WaterJug(initial, goal)

print("Verifying successor function:")
jug.verify_successor()

print("\nBFS Solution Path:")
bfs_path = jug.bfs()
for state in bfs_path: # type: ignore
    print(state)

print("\nDFS Solution Path:")
dfs_path = jug.dfs()
for state in dfs_path: # type: ignore
    print(state)
