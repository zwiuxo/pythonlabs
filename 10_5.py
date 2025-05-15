import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 15, num=50)
y = np.linspace(0, 10, num=50)
X, Y = np.meshgrid(x, y)
Z = (X - Y)**2 / X.size

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Surface Z')


ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_zscale('log')
ax2.set_title('Surface log Z')

plt.tight_layout()
plt.show()