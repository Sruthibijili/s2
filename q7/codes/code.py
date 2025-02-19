import subprocess
import matplotlib.pyplot as plt
import numpy as np

def call_c_program():
    # Compile the C program (ensure gcc is installed)
    subprocess.run(["gcc", "ccode.c", "-o", "generate_probabilities"], check=True)
    
    # Run the compiled C program and capture output
    result = subprocess.run(["./generate_probabilities"], capture_output=True, text=True)
    
    # Extract probabilities from output
    probabilities = list(map(float, result.stdout.strip().split()))
    return probabilities

# Call the C function and get probabilities
P_AB, P_BC, P_CA = call_c_program()

# Print results
print(f"P(A ∩ B): {P_AB:.3f}")
print(f"P(B ∩ C): {P_BC:.3f}")
print(f"P(C ∩ A): {P_CA:.3f}")

# Theoretical values (example, modify as needed)
P_AB_theory = 0.0
P_BC_theory = 0.0
P_CA_theory = (1/9) + (1/36)  # Example theoretical values

# Data for plotting
labels = ['P(A ∩ B)', 'P(B ∩ C)', 'P(C ∩ A)']
x_pos = np.arange(len(labels))
simulated_values = [P_AB, P_BC, P_CA]
theoretical_values = [P_AB_theory, P_BC_theory, P_CA_theory]

plt.figure(figsize=(8, 5))

# Plot stem-like lines for both simulated and theoretical values at the same x positions
plt.stem(x_pos, simulated_values, linefmt='b-', markerfmt='bo', basefmt=' ', label='Simulation')
plt.stem(x_pos, theoretical_values, linefmt='r--', markerfmt='ro', basefmt=' ', label='Theoretical')

plt.xlabel("Events")
plt.ylabel("Probability")
plt.title("Theoretical vs Simulated Probability of Intersections")
plt.xticks(x_pos, labels)
plt.ylim(0, 0.2)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show probability values on top of stems
for i, (sim, theo) in enumerate(zip(simulated_values, theoretical_values)):
    plt.text(i, sim + 0.005, f"{sim:.3f}", ha='center', fontsize=12, color='blue')
    plt.text(i, theo + 0.005, f"{theo:.3f}", ha='center', fontsize=12, color='red')

plt.show()
