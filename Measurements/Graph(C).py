#This code produces graph c
import numpy as np
import matplotlib.pyplot as plt

# Penny measurements
trials = np.array([1, 2, 3, 4])

diameters = np.array([
    1.90,
    1.90,
    1.89,
    1.90
])  # cm

thicknesses = np.array([
    0.11,
    0.10,
    0.10,
    0.11
])  # cm

masses = np.array([
    2.507,
    2.508,
    2.506,
    2.508
])  # g

# Calculate volume of each penny
# V = pi * (diameter / 2)^2 * thickness
volumes = np.pi * (diameters / 2)**2 * thicknesses

# Calculate density
densities = masses / volumes

# Calculate average and sample standard deviation
average = np.mean(densities)
std_dev = np.std(densities, ddof=1)

# True density of a penny
true_density = 8.8  # g/cm^3

# Print calculated values
print("Penny Measurements:")
for i in range(len(trials)):
    print(f"Trial {i+1}:")
    print(f"  Volume = {volumes[i]:.4f} cm³")
    print(f"  Density = {densities[i]:.4f} g/cm³")

print(f"\nAverage density: {average:.4f} g/cm³")
print(f"Standard deviation: {std_dev:.4f} g/cm³")

# Create bar graph
plt.figure(figsize=(9, 6))

plt.bar(
    trials,
    densities,
    yerr=std_dev,
    capsize=7,
    color="saddlebrown",
    edgecolor="black",
    error_kw={
        "elinewidth": 2,
        "ecolor": "black"
    },
    label="Measured Density ± 1 SD"
)

# Average density line
plt.axhline(
    average,
    color="red",
    linewidth=2,
    linestyle="-",
    label=f"Average = {average:.4f} g/cm³"
)

# True density line
plt.axhline(
    true_density,
    color="green",
    linewidth=2,
    linestyle="--",
    label=f"True Density = {true_density:.1f} g/cm³"
)

# Axis labels
plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/cm³)", fontsize=12)

# X-axis
plt.xticks(trials, ["1", "2", "3", "4"])

# Y-axis range
plt.ylim(6.5, 9.5)

# Title
plt.title("Density of a Penny", fontsize=14)

# Grid
plt.grid(axis="y", alpha=0.3)

# Legend
plt.legend()

plt.tight_layout()
plt.show()
