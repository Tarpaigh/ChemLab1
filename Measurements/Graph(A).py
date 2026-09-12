#This code produces the bar graph for the measurements lab
import numpy as np
import matplotlib.pyplot as plt

# Raw data
empty_cylinder_mass = 42.67  # g

trials = np.array([1, 2, 3, 4, 5])

volumes = np.array([
    10.0,
    20.0,
    30.0,
    40.0,
    50.0
])  # mL

total_masses = np.array([
    52.58,
    62.493,
    72.39,
    82.31,
    92.24
])  # g

# Calculate mass of water
water_masses = total_masses - empty_cylinder_mass

# Calculate density for each trial
densities = water_masses / volumes

# Calculate average and sample standard deviation
average = np.mean(densities)
std_dev = np.std(densities, ddof=1)

# True density of water
true_density = 0.99802  # g/mL

# Print calculated values
print("Densities:")
for i, density in enumerate(densities, start=1):
    print(f"Trial {i}: {density:.4f} g/mL")

print(f"\nAverage density: {average:.4f} g/mL")
print(f"Standard deviation: {std_dev:.4f} g/mL")

# Create the bar graph
plt.figure(figsize=(9, 6))

plt.bar(
    trials,
    densities,
    yerr=std_dev,
    capsize=7,
    color="skyblue",
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
    label=f"Average = {average:.4f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    color="green",
    linewidth=2,
    linestyle="--",
    label=f"True Density = {true_density:.5f} g/mL"
)

# Axis labels
plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/mL)", fontsize=12)

# X-axis: Trials 1–5
plt.xticks(trials, ["1", "2", "3", "4", "5"])

# Y-axis range
plt.ylim(0.98, 1.01)

# Title
plt.title("Density of Water (Graduated Cylinder)", fontsize=14)

# Grid
plt.grid(axis="y", alpha=0.3)

# Legend
plt.legend()

plt.tight_layout()
plt.show()
