import math


class SimulatedAnnealingDemo:
    def __init__(self, delta_e):
        self.delta_e = delta_e  # Inferior move cost

    # Acceptance probability function
    def acceptance_probability(self, T):
        return math.exp(-self.delta_e / T)

    # Temperature schedule (cooling)
    def temperature_schedule(self, T0, alpha, steps):
        T = T0
        for i in range(steps):
            yield T
            T *= alpha


# Driver Code
delta_e = 5          # Inferior move cost
initial_temp = 100   # High initial temperature
cooling_rate = 0.8   # Temperature decay
steps = 10

sa = SimulatedAnnealingDemo(delta_e)

print("Temperature\tAcceptance Probability")
print("------------------------------------")

for T in sa.temperature_schedule(initial_temp, cooling_rate, steps):
    prob = sa.acceptance_probability(T)
    print(f"{T:10.2f}\t{prob:.6f}")
