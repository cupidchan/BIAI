import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting random seed for reproducibility
np.random.seed(42)

# Time (in weeks)
weeks = np.arange(1, 9)

# Generating synthetic growth data
sunlight_mean = 5 * weeks + np.random.normal(0, 2, len(weeks))
artificial_mean = 4 * weeks + np.random.normal(0, 2, len(weeks))
darkness_mean = 2 + np.random.normal(0, 1, len(weeks))

# Generating synthetic standard deviations (variability in measurements)
sunlight_std = np.random.uniform(2, 5, len(weeks))
artificial_std = np.random.uniform(2, 5, len(weeks))
darkness_std = np.random.uniform(1, 3, len(weeks))

# Set a modern color palette from seaborn
colors = sns.color_palette("tab10")

# Plotting
plt.figure(figsize=(10, 6))

# Plotting mean growth and shaded error for Natural Sunlight
plt.plot(weeks, sunlight_mean, '-o', color=colors[0], label='Natural Sunlight')
plt.fill_between(weeks, sunlight_mean - sunlight_std,
                 sunlight_mean + sunlight_std, color=colors[0], alpha=0.2)

# Plotting mean growth and shaded error for Artificial Light
plt.plot(weeks, artificial_mean, '-s',
         color=colors[1], label='Artificial Light')
plt.fill_between(weeks, artificial_mean - artificial_std,
                 artificial_mean + artificial_std, color=colors[1], alpha=0.2)

# Plotting mean growth and shaded error for Darkness
plt.plot(weeks, darkness_mean, '-^', color=colors[2], label='Darkness')
plt.fill_between(weeks, darkness_mean - darkness_std,
                 darkness_mean + darkness_std, color=colors[2], alpha=0.2)

plt.xlabel('Weeks')
plt.ylabel('Average Plant Height (cm)')
plt.title('Growth of Plants under Different Light Conditions')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
