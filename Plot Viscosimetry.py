import numpy as np
import matplotlib.pyplot as plt
# Data
M = np.array([5380, 10100, 20500, 40000, 97300, 191000])
eta = np.array([6.59, 9.00, 12.3, 17.2, 27.3, 38.0])

# Take logarithms (base 10)
logM = np.log10(M)
logEta = np.log10(eta)

# Linear regression: log(η) = a*log(M) + logK
a, logK = np.polyfit(logM, logEta, 1)
K = 10**logK

# Print the results
print(f"Slope (a): {a:.3f}")
print(f"Intercept (logK): {logK:.3f}")
print(f"K value: {K:.5f}")

# Plot
plt.scatter(logM, logEta, label='Data')
plt.plot(logM, a*logM + logK, 'r-', label=f'Fit: a={a:.3f}')
plt.xlabel('log(M)')
plt.ylabel('log([η])')
plt.legend()
plt.grid(True)
plt.show()