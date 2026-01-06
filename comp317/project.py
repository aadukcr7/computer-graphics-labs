import numpy as np
import matplotlib.pyplot as plt

print("=" * 50)
print("M/M/1 QUEUE SIMULATION")
print("=" * 50)

# Get user input for service rate
mu = float(input("Enter service rate (μ): "))

# Get user input for arrival rate
print(f"\nNote: Arrival rate (λ) must be less than {mu} for system stability")
lamda_max = float(input(f"Enter maximum arrival rate (λ < {mu}): "))

# Validate input
if lamda_max >= mu:
    print(f"\nWarning: λ adjusted to {mu * 0.95} for stability")
    lamda_max = mu * 0.95

# Arrival rates (lambda < mu)
lamda = np.linspace(0.1, lamda_max, 100)

# Lq formula for M/M/1
Lq = (lamda ** 2) / (mu * (mu - lamda))

# Plot
plt.figure()
plt.plot(lamda, Lq)
plt.xlabel("Arrival Rate (λ)")
plt.ylabel("Average Queue Length (Lq)")
plt.title(f"M/M/1 Queue: Lq vs λ (μ = {mu})")
plt.grid(True)
print("\nDisplaying plot...")
plt.show()
