import numpy as np
import matplotlib.pyplot as plt

# Setting random seed for reproducibility
np.random.seed(42)

# Generating square footage data for 200 houses
x = np.random.uniform(500, 5000, 200)

# Generating synthetic house prices: base price is $100 per square foot with some noise
y = x * 100 + np.random.normal(0, 20000, 200)

# Generating confidence levels: highest confidence for medium-sized houses
confidence = 1 - ((x - 2500) / 2500)**2
confidence = np.clip(confidence + np.random.normal(0, 0.1, 200), 0, 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=confidence, cmap='RdYlBu_r', alpha=0.7)
plt.colorbar(label='Confidence Level')
plt.xlabel('Square Footage')
plt.ylabel('Predicted House Price ($)')
plt.title('Predicted House Prices vs. Square Footage with Confidence Levels')
plt.show()
