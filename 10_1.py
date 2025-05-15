import matplotlib.pyplot as plt
from scipy.special import legendre
import numpy as np

x = np.arange(-1, 1, 0.01)
colors = ["green", "blue", "purple", "orange", "yellow", "brown", "black"]
plt.figure(figsize=(8, 5))
for n, color in enumerate(colors, start=1):
    Pn = legendre(n)
    plt.plot(x, Pn(x), color=color, label=f"n = {n}")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.title("Полиномы Лежандра")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()