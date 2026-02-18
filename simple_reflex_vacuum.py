import random


class SimpleReflexVacuumAgent:
    def __init__(self, size=(3, 3)):
        self.size = size
        self.room = [
            [random.choice([0, 1]) for _ in range(size[1])] for _ in range(size[0])
        ]
        self.position = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))

    def perceive(self):
        x, y = self.position
        return self.room[x][y]

    def act(self):
        x, y = self.position
        if self.perceive() == 1:
            print(f"Dirty at {self.position} → SUCK")
            self.room[x][y] = 0
        else:
            self.move()

    def move(self):
        x, y = self.position
        moves = []
        if x > 0:
            moves.append((x - 1, y))
        if x < self.size[0] - 1:
            moves.append((x + 1, y))
        if y > 0:
            moves.append((x, y - 1))
        if y < self.size[1] - 1:
            moves.append((x, y + 1))
        self.position = random.choice(moves)
        print(f"Moved to {self.position}")

    def run(self, steps=20):
        for i in range(steps):
            print(f"\nStep {i+1}")
            self.act()

agent = SimpleReflexVacuumAgent((3, 3))
agent.run()
