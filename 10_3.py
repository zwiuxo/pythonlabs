import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 100, num=5000)
fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    x = np.sin(0.1 * (frame + 1) * t)
    y = np.sin(t)
    ax.plot(x, y, color='green')

ani = FuncAnimation(fig, update, frames=24)
plt.show()