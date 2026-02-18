# Block World Planner (Goal Stack Planning)

class BlockWorld:
    def __init__(self, initial_state, goal_state):
        self.state = initial_state  # e.g., {'A':'table', 'B':'A', 'C':'table'}
        self.goal = goal_state
        self.actions = []

    def clear(self, block):
        # Returns True if the block has nothing on top
        return all(v != block for v in self.state.values())

    def move(self, block, destination):
        # Move block to destination (table or another block)
        print(f"Moving {block} to {destination}")
        self.state[block] = destination
        self.actions.append((block, destination))

    def is_goal(self):
        return self.state == self.goal

    def plan(self):
        # Very simple recursive planner
        for block, target in self.goal.items():
            # If block already in place, skip
            if self.state[block] == target:
                continue

            # If something is on top, move it to table first
            for b, pos in self.state.items():
                if pos == block:
                    if self.clear(b):
                        self.move(b, 'table')
                    else:
                        self.plan()  # recursive fix

            # Move block to target if clear
            if self.clear(block):
                self.move(block, target)
            else:
                # Clear first
                for b, pos in self.state.items():
                    if pos == block:
                        self.move(b, 'table')
                self.move(block, target)

# Example usage
initial_state = {'A':'table', 'B':'table', 'C':'A'}
goal_state    = {'A':'B', 'B':'C', 'C':'table'}

bw = BlockWorld(initial_state, goal_state)
bw.plan()

print("\nFinal State:", bw.state)
print("Actions Taken:", bw.actions)