#This code produces the Beer graph for the spectroscopy lab
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Calcium Atomic Absorption Spectroscopy Calibration
# --------------------------------------------------

# Experimental calibration data
concentration = np.array([0, 2, 4, 6, 8, 10, 15])  # Ca2+ concentration (ppm)
absorbance = np.array([0.000, 0.061, 0.120, 0.190,
                       0.245, 0.310, 0.462])       # Absorbance

# Calculate linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Calculate predicted absorbance values
predicted = slope * concentration + intercept

# Calculate R-squared
ss_res = np.sum((absorbance - predicted) ** 2)
ss_tot = np.sum((absorbance - np.mean(absorbance)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

# --------------------------------------------------
# Calculate photon energy using Eq. 1: E = hc/lambda
# --------------------------------------------------

h = 6.626e-34       # Planck's constant (J s)
c = 2.998e8         # Speed of light (m/s)
wavelength_nm = 422.7

# Convert wavelength from nm to m
wavelength_m = wavelength_nm * 1e-9

# Calculate energy per photon
photon_energy = (h * c) / wavelength_m

# --------------------------------------------------
# Print results
# --------------------------------------------------

print("CALCIUM AA CALIBRATION RESULTS")
print("--------------------------------")
print(f"Slope: {slope:.5f}")
print(f"Intercept: {intercept:.5f}")
print(f"Regression equation: y = {slope:.5f}x + {intercept:.5f}")
print(f"R-squared: {r_squared:.5f}")
print()
print("AA PHOTON ENERGY")
print("--------------------------------")
print(f"Monitoring wavelength: {wavelength_nm:.1f} nm")
print(f"Photon energy: {photon_energy:.4e} J/photon")

# --------------------------------------------------
# Create calibration curve
# --------------------------------------------------

plt.figure(figsize=(10, 7))

# Plot experimental data
plt.scatter(
    concentration,
    absorbance,
    color="blue",
    edgecolor="black",
    label="Experimental Data",
    zorder=3
)

# Plot best-fit regression line
x_line = np.linspace(min(concentration), max(concentration), 200)
y_line = slope * x_line + intercept

plt.plot(
    x_line,
    y_line,
    color="red",
    linewidth=2,
    label="Linear Regression"
)

# --------------------------------------------------
# Add regression equation, R-squared, and photon energy
# --------------------------------------------------

equation_text = (
    f"y = {slope:.5f}x + {intercept:.5f}\n"
    f"$R^2$ = {r_squared:.5f}\n\n"
    f"Absorbance = ({slope:.5f} x Ca$^{{2+}}$ concentration in ppm)\n"
    f"+ ({intercept:.5f})\n\n"
    f"AA Monitoring Wavelength = {wavelength_nm:.1f} nm\n"
    f"Photon Energy = {photon_energy:.4e} J/photon"
)

plt.text(
    0.52, 0.05,
    equation_text,
    transform=plt.gca().transAxes,
    fontsize=9,
    verticalalignment="bottom",
    bbox=dict(
        boxstyle="round",
        facecolor="white",
        edgecolor="gray",
        alpha=0.95
    )
)

# --------------------------------------------------
# Graph formatting
# --------------------------------------------------

plt.title(
    "Calcium Calibration Curve — Atomic Absorption Spectroscopy",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Calcium Ion Concentration (ppm by mass)", fontsize=12)
plt.ylabel("Absorbance (unitless)", fontsize=12)

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Save high-resolution graph
plt.savefig(
    "Calcium_Calibration_Curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()