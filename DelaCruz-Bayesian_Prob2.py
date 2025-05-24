"""
Created on Fri May 23 2025  14:25:18

@author: Christine D. Dela Cruz
"""

import numpy as np
import matplotlib.pyplot as plt

# Given Probabilities
p_disease = 0.005
p_no_disease = 1 - p_disease
p_pos_given_disease = 0.99
p_pos_given_no_disease = 0.05

# Probability of positive result
p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)

# Posterior probability using Bayes' Theorem
p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos
p_no_disease_given_pos = (p_pos_given_no_disease * p_no_disease) / p_pos

# Sample from prior and posterior
prior_samples = np.random.choice(['Disease', 'No Disease'], size=1000, p=[p_disease, p_no_disease])
posterior_samples = np.random.choice(['Disease', 'No Disease'], size=1000, p=[p_disease_given_pos, p_no_disease_given_pos])

# Plot
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(prior_samples, bins=2, color='yellow', edgecolor='skyblue', rwidth=0.8)
plt.title('Prior: Probability of Disease in Population')
plt.xlabel('Condition')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.hist(posterior_samples, bins=2, color='pink', edgecolor='black', rwidth=0.8)
plt.title('Posterior: Probability of Disease Given Positive Test')
plt.xlabel('Condition')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# Print results
print("P(Disease | Positive Test):", round(p_disease_given_pos, 4))
print("P(No Disease | Positive Test):", round(p_no_disease_given_pos, 4))
