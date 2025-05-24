"""
Created on Sat May 24, 2025  18:55:12

@author: Christine D. Dela Cruz
"""

import numpy as np
import matplotlib.pyplot as plt

# Observed data
items_checked = 200
defective_items = 12

# Prior
alpha_prior = 1
beta_prior = 5

# Update to get posterior
alpha_posterior = alpha_prior + defective_items
beta_posterior = beta_prior + (items_checked - defective_items)

# Sample from prior and posterior
prior_samples = np.random.beta(alpha_prior, beta_prior, 1000)
posterior_samples = np.random.beta(alpha_posterior, beta_posterior, 1000)

# Plot the prior and posterior
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(prior_samples, bins=30, color='skyblue', edgecolor='black')
plt.title('Prior Distribution of Defect Rate')
plt.xlabel('Defect Rate')
plt.ylabel('Density')

plt.subplot(1, 2, 2)
plt.hist(posterior_samples, bins=30, color='yellow', edgecolor='black')
plt.title('Posterior Distribution of Defect Rate')
plt.xlabel('Defect Rate')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

# Summary
mean_defect_rate = alpha_posterior / (alpha_posterior + beta_posterior)
print("Estimated defect rate (mean):", round(mean_defect_rate, 4))