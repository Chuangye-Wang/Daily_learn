import numpy as np
import matplotlib.pyplot as plt

# Define heart curve equations

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the heart curve
plt.figure(figsize=(6, 6))
plt.plot(x, y, "r")  # 'r' for red color
plt.fill(x, y, "r", alpha=0.3)  # Fill with red color with some transparency

# Formatting the plot
plt.axis("equal")  # Equal aspect ratio to maintain shape
plt.axis("off")  # Hide axes for better aesthetics
plt.title("Heart Curve", fontsize=14)
plt.savefig("love_heart.png")

# Show the plot
plt.show()
