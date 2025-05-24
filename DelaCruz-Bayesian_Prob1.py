"""
Created on Fri May 23, 2025  09:44:29

@author: Christine D. Dela Cruz
"""

import numpy as np
import matplotlib.pyplot as plt

# Flip the coin 10 times
heads = 7
tails = 3

# Define the prior (Beta distribution)
alpha_prior = 2
beta_prior = 3

# Update to get posterior
alpha_posterior = alpha_prior + heads
beta_posterior = beta_prior + tails

# Sample from prior and posterior
prior_samples = np.random.beta(alpha_prior, beta_prior, 1000)
posterior_samples = np.random.beta(alpha_posterior, beta_posterior, 1000)

# Plot the prior and posterior
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(prior_samples, bins=30, color='blue', edgecolor='black')
plt.title('Prior Distribution of Probability of Heads')
plt.xlabel('Probability of Heads')
plt.ylabel('Density')

plt.subplot(1, 2, 2)
plt.hist(posterior_samples, bins=30, color='brown', edgecolor='black')
plt.title('Posterior Distribution of Probability of Heads')
plt.xlabel('Probability of Heads')
plt.ylabel('Density')

plt.tight_layout()
plt.show()
