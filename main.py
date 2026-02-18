class BlocksWorldHeuristic:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def get_support_structure(self, state, block):
        support = [block]
        while state[block] != "Table":
            block = state[block]
            support.append(block)
        return support

    def heuristic(self, state):
        score = 0

        for block in state:
            support = self.get_support_structure(state, block)

            if state[block] == self.goal_state.get(block):
                # Correct support structure
                score += len(support)
            else:
                # Wrong support structure
                score -= len(support)

        return score


# Example
goal_state = {"A": "B", "B": "C", "C": "Table"}

state = {"A": "Table", "B": "C", "C": "Table"}

bw = BlocksWorldHeuristic(goal_state)

print("Heuristic value e(p):", bw.heuristic(state))
