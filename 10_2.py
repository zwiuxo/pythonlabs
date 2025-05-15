import matplotlib.pyplot as plt
import numpy as np


ratios = [(3,2), (3,4), (5,4), (5,6)]
colors = ['green', 'red', 'yellow', 'black']
t = np.linspace(0, 2*np.pi, num=500)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))
for ax, (a,b), color in zip(axes.flatten(), ratios, colors):
    x = np.sin(a * t)
    y = np.sin(b * t)
    ax.plot(x, y, color=color)
    ax.set_title(f'{a}:{b}')
    ax.set_aspect('equal')
    ax.grid(True)

plt.tight_layout()
plt.show()