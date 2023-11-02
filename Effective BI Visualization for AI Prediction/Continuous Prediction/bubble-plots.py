from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting random seed for reproducibility
np.random.seed(42)

# Generating synthetic data
n_users = 200
user_engagement = np.random.uniform(1, 100, n_users)  # Score from 1 to 100
# Base revenue plus some proportion of engagement
expected_revenue = 50 + 0.5 * user_engagement + \
    np.random.normal(0, 10, n_users)
confidence = np.clip(np.random.normal(0.5, 0.2, n_users),
                     0, 1)  # Confidence values between 0 and 1

# Scale confidence for visualization (bubble size)
bubble_size = confidence * 1000  # Scale factor for better visual

# Assign membership tiers to users (as integers 0-3 for Bronze to Platinum)
membership_tiers = np.random.choice([0, 1, 2, 3], size=n_users, p=[
                                    0.4, 0.3, 0.2, 0.1])  # Adjust probabilities as needed

# Map membership tiers to colors (using RGBA or hex values)
tier_colors = {
    0: '#cd7f32',  # Bronze
    1: '#c0c0c0',  # Silver
    2: '#ffd700',  # Gold
    # Platinum (simulated with a light gray since "platinum" isn't a standard color)
    3: '#e5e4e2'
}
colors = [tier_colors[tier] for tier in membership_tiers]

# Plotting
plt.figure(figsize=(10, 6))
scatter = plt.scatter(user_engagement, expected_revenue,
                      s=bubble_size, c=colors, edgecolor='w', alpha=0.6)

# Adding custom legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=tier_colors[0], markersize=10, label='Bronze'),
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=tier_colors[1], markersize=10, label='Silver'),
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=tier_colors[2], markersize=10, label='Gold'),
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=tier_colors[3], markersize=10, label='Platinum')
]
plt.legend(handles=legend_elements, title="Membership Tiers", loc="upper left")

plt.xlabel('User Engagement Score')
plt.ylabel('Expected Revenue ($)')
plt.title('E-commerce Product Recommendations by Membership Tier')
plt.tight_layout()
plt.show()
