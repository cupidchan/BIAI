import numpy as np
import matplotlib.pyplot as plt

# Setting random seed for reproducibility
np.random.seed(42)

# Generating synthetic advertising spend data
x = np.linspace(0, 100, 20)  # Online Advertising Spend (in $1000s)
y = np.linspace(0, 100, 20)  # Television Advertising Spend (in $1000s)
X, Y = np.meshgrid(x, y)

# Generating synthetic sales predictions based on advertising spend
# Assume a linear relationship with added noise for simplicity
Z = 50 + 0.5 * X + 0.4 * Y + np.random.normal(0, 10, X.shape)

# Generating synthetic confidence values (higher confidence for higher sales values)
# Clip values to ensure a minimum confidence level
confidence = np.clip(Z / Z.max(), 0.5, 1)

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(
    confidence), cmap='viridis', edgecolor='k', linewidth=0.5)

# Adding color bar to indicate confidence level
cbar = fig.colorbar(surf, ax=ax, shrink=0.7, aspect=5)
cbar.set_label('Confidence Level')

ax.set_xlabel('Online Advertising Spend ($1000s)')
ax.set_ylabel('Television Advertising Spend ($1000s)')
ax.set_zlabel('Predicted Sales ($)')
ax.set_title('Predicted Sales Based on Advertising Spend')
plt.tight_layout()
plt.show()
