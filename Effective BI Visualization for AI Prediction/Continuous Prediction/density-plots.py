import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting random seed for reproducibility
np.random.seed(42)

# Generating synthetic predicted and actual house prices
n_houses = 1000
# Predicted prices between $100,000 and $500,000
predicted_prices = np.random.uniform(100000, 500000, n_houses)
# Random residuals with a slight trend
residuals = np.random.normal(0, 20000, n_houses) + (0.05 * predicted_prices)
actual_prices = predicted_prices + residuals

# Binning the predicted prices to group them
bins = np.linspace(100000, 500000, 20)
labels = (bins[:-1] + bins[1:]) / 2  # Using mid-points of bins as labels
predicted_price_bins = np.digitize(predicted_prices, bins) - 1

# Plotting
plt.figure(figsize=(12, 7))

for i, label in enumerate(labels):
    subset_residuals = residuals[predicted_price_bins == i]
    if len(subset_residuals) > 10:  # Ensure there's enough data to create a meaningful density plot
        sns.kdeplot(subset_residuals,
                    label=f'Predicted: ${label:.2f}', fill=True)

plt.axvline(0, color='red', linestyle='--', label="Zero Residual Line")
plt.xlabel('Residual Value ($)')
plt.ylabel('Density')
plt.title('Density Plots of Residuals for Different Predicted House Prices')
plt.legend()
plt.tight_layout()
plt.show()
