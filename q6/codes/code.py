import numpy as np
import matplotlib.pyplot as plt

# Define the lines
def line1(u1):
    return (12 - 3 * u1) / 2

def line2(u1):
    return (13 -2 * u1) / 3

# Define the range of u1
u1 = np.linspace(-2, 4, 1000)

# Compute v values for both lines
v1 = line1(u1)
v2 = line2(u1)

# Solve for the intersection point
A = np.array([[3, 2], [2, 3]])
b = np.array([12, 13])
intersection = np.linalg.solve(A, b)  # [u, v]

# Plot the lines
plt.figure(figsize=(8, 6))
plt.plot(u1, v1, label='3u + 2v = 12', color='blue')
plt.plot(u1, v2, label='2u + 3v = 13', color='orange')

# Mark the intersection point
plt.scatter(intersection[0], intersection[1], color='red', label=f'Intersection ({intersection[0]:.2f}, {intersection[1]:.2f})', zorder=5)
plt.text(intersection[0] + 0.1, intersection[1] - 0.1, 
         f'({intersection[0]:.2f}, {intersection[1]:.2f})', 
         fontsize=12, color='red')

# Customize labels and styling
plt.xlabel(r'$u = \frac{1}{x}$', fontsize=12)
plt.ylabel(r'$v = \frac{1}{y}$', fontsize=12)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=10)

# Show the plot
plt.title("Intersection of Lines in u-v Space", fontsize=14)
plt.savefig('../figs/fig.pdf')
plt.show()

