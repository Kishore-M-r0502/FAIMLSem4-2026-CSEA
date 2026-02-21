import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load data from CSV
df = pd.read_csv('songs.csv')
loudness_data = df['loudness'].values


# Compute statistics

mu = np.mean(loudness_data)
sigma = np.std(loudness_data)

print(f"Mean loudness: {mu:.3f} dB")
print(f"Standard deviation: {sigma:.3f} dB")
print(f"Min loudness: {np.min(loudness_data):.3f} dB")
print(f"Max loudness: {np.max(loudness_data):.3f} dB")


# Prepare normal distribution curve

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = norm.pdf(x, mu, sigma)


# Plot histogram
plt.figure(figsize=(10,6))

# Overlay normal curve
plt.plot(x, pdf, 'r', linewidth=2, label='Normal Curve')


# Highlight ±1σ, ±2σ, ±3σ ranges

colors = ['#32cc68','#d37919','#2f53a7'] 

for i, multiplier in enumerate([1,2,3]):
    start = mu - multiplier*sigma
    end = mu + multiplier*sigma
    plt.axvspan(start, end, color=colors[i], alpha=0.2, label=f'±{multiplier}σ')


#  Labels and legend

plt.xlabel('Loudness (dB)')
plt.ylabel('Probability Density')
plt.title('Loudness Distribution with Normal Curve and σ Ranges')
plt.legend()
plt.grid(False)
plt.show()
